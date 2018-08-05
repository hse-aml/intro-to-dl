#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random
import tqdm_utils


def test_vocab(vocab, PAD, UNK, START, END):
    return [
        len(vocab),
        len(np.unique(list(vocab.values()))),
        int(all([_ in vocab for _ in [PAD, UNK, START, END]]))
    ]


def test_captions_indexing(train_captions_indexed, vocab, UNK):
    starts = set()
    ends = set()
    between = set()
    unk_count = 0
    for caps in train_captions_indexed:
        for cap in caps:
            starts.add(cap[0])
            between.update(cap[1:-1])
            ends.add(cap[-1])
            for w in cap:
                if w == vocab[UNK]:
                    unk_count += 1
    return [
        len(starts),
        len(ends),
        len(between),
        len(between | starts | ends),
        int(all([isinstance(x, int) for x in (between | starts | ends)])),
        unk_count
    ]


def test_captions_batching(batch_captions_to_matrix):
    return (batch_captions_to_matrix([[1, 2, 3], [4, 5]], -1, max_len=None).ravel().tolist()
            + batch_captions_to_matrix([[1, 2, 3], [4, 5]], -1, max_len=2).ravel().tolist()
            + batch_captions_to_matrix([[1, 2, 3], [4, 5]], -1, max_len=10).ravel().tolist())


def get_feed_dict_for_testing(decoder, IMG_EMBED_SIZE, vocab):
    return {
        decoder.img_embeds: np.random.random((32, IMG_EMBED_SIZE)),
        decoder.sentences: np.random.randint(0, len(vocab), (32, 20))
    }


def test_decoder_shapes(decoder, IMG_EMBED_SIZE, vocab, s):
    tensors_to_test = [
        decoder.h0,
        decoder.word_embeds,
        decoder.flat_hidden_states,
        decoder.flat_token_logits,
        decoder.flat_ground_truth,
        decoder.flat_loss_mask,
        decoder.loss
    ]
    all_shapes = []
    for t in tensors_to_test:
        _ = s.run(t, feed_dict=get_feed_dict_for_testing(decoder, IMG_EMBED_SIZE, vocab))
        all_shapes.extend(_.shape)
    return all_shapes


def test_random_decoder_loss(decoder, IMG_EMBED_SIZE, vocab, s):
    loss = s.run(decoder.loss, feed_dict=get_feed_dict_for_testing(decoder, IMG_EMBED_SIZE, vocab))
    return loss


def test_validation_loss(decoder, s, generate_batch, val_img_embeds, val_captions_indexed):
    np.random.seed(300)
    random.seed(300)
    val_loss = 0
    batches_for_eval = 1000
    for _ in tqdm_utils.tqdm_notebook_failsafe(range(batches_for_eval)):
        val_loss += s.run(decoder.loss, generate_batch(val_img_embeds,
                                                       val_captions_indexed,
                                                       32,
                                                       20))
    val_loss /= 1000.
    return val_loss
