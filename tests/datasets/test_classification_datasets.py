"""Unit tests for 
"""
import pytest
import torch

from pyrelational.datasets import (
    SynthClass1,
    SynthClass2,
    SynthClass3,
    BreastCancerDataset,
    DigitDataset,
    FashionMNIST,
    UCIGlass,
    UCIParkinsons,
    UCISeeds,
    StriatumDataset,
    GaussianCloudsDataset,
    Checkerboard2x2Dataset,
    Checkerboard4x4Dataset,
)


def test_SynthClass1():
    dataset = SynthClass1()
    assert len(dataset) == 500
    assert len(dataset.data_splits) == 5

    dataset = SynthClass1(n_splits=3, size=1000)
    assert len(dataset) == 1000
    assert len(dataset.data_splits) == 3

def test_SynthClass2():
    dataset = SynthClass2()
    assert len(dataset) == 500
    assert len(dataset.data_splits) == 5

    dataset = SynthClass2(n_splits=3, size=1000)
    assert len(dataset) == 1000
    assert len(dataset.data_splits) == 3

def test_SynthClass3():
    dataset = SynthClass3()
    assert len(dataset) == 500
    assert len(dataset.data_splits) == 5

    dataset = SynthClass3(n_splits=3, size=2000)
    assert len(dataset) == 2000
    assert len(dataset.data_splits) == 3

def test_BreastCancerDataset():
    dataset = BreastCancerDataset()
    assert len(dataset) == 569
    assert dataset.x.shape[1] == 30
    assert len(dataset.data_splits) == 5

def test_DigitDataset():
    dataset = DigitDataset()
    assert len(dataset) == 1797
    assert dataset.x.shape[1] == 64
    assert len(dataset.data_splits) == 5

def test_FashionMNIST():
    dataset = FashionMNIST()
    assert len(dataset) == 70000
    assert dataset.x.shape[1] == 784
    assert len(dataset.data_splits) == 5
