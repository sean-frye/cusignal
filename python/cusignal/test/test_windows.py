# Copyright (c) 2019-2020, NVIDIA CORPORATION.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cupy as cp
import cusignal
import pytest

from cusignal.test.utils import array_equal
from scipy import signal


class TestWindows:
    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_general_cosine(self, num_samps):
        HFT90D = [1, 1.942604, 1.340318, 0.440811, 0.043097]
        cpu_window = signal.windows.general_cosine(
            num_samps, HFT90D, sym=False
        )
        gpu_window = cp.asnumpy(
            cusignal.windows.general_cosine(num_samps, HFT90D, sym=False)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_boxcar(self, num_samps):
        cpu_window = signal.windows.boxcar(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.boxcar(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_triang(self, num_samps):
        cpu_window = signal.windows.triang(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.triang(num_samps))
        assert array_equal(cpu_window, gpu_window)

    """
    This isn't preferred, but Parzen is technically broken until
    cuPy 8.0. Commenting out until cuSignal 0.16
    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_parzen(self, num_samps):
        cpu_window = signal.windows.parzen(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.parzen(num_samps))
        assert array_equal(cpu_window, gpu_window)
    """

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_bohman(self, num_samps):
        cpu_window = signal.windows.bohman(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.bohman(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_blackman(self, num_samps):
        cpu_window = signal.windows.blackman(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.blackman(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_nuttall(self, num_samps):
        cpu_window = signal.windows.nuttall(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.nuttall(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_blackmanharris(self, num_samps):
        cpu_window = signal.windows.blackmanharris(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.blackmanharris(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_flattop(self, num_samps):
        cpu_window = signal.windows.flattop(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.flattop(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_barlett(self, num_samps):
        cpu_window = signal.windows.bartlett(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.bartlett(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_hann(self, num_samps):
        cpu_window = signal.windows.hann(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.hann(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("alpha", [0.25, 0.5])
    def test_tukey(self, num_samps, alpha):
        cpu_window = signal.windows.tukey(num_samps, alpha, sym=True)
        gpu_window = cp.asnumpy(
            cusignal.windows.tukey(num_samps, alpha, sym=True)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_barthann(self, num_samps):
        cpu_window = signal.windows.barthann(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.barthann(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("alpha", [0.25, 0.5])
    def test_general_hamming(self, num_samps, alpha):
        cpu_window = signal.windows.general_hamming(num_samps, alpha, sym=True)
        gpu_window = cp.asnumpy(
            cusignal.windows.general_hamming(num_samps, alpha, sym=True)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_hamming(self, num_samps):
        cpu_window = signal.windows.hamming(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.hamming(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("beta", [0.25, 0.5])
    def test_kaiser(self, num_samps, beta):
        cpu_window = signal.windows.kaiser(num_samps, beta, sym=True)
        gpu_window = cp.asnumpy(
            cusignal.windows.kaiser(num_samps, beta, sym=True)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("std", [3, 7])
    def test_gaussian(self, num_samps, std):
        cpu_window = signal.windows.gaussian(num_samps, std)
        gpu_window = cp.asnumpy(cusignal.windows.gaussian(num_samps, std))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("p", [0.75, 1.5])
    @pytest.mark.parametrize("std", [3, 7])
    def test_general_gaussian(self, num_samps, p, std):
        cpu_window = signal.windows.general_gaussian(num_samps, p, std)
        gpu_window = cp.asnumpy(
            cusignal.windows.general_gaussian(num_samps, p, std)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("at", [50, 100])
    def test_chebwin(self, num_samps, at):
        cpu_window = signal.windows.chebwin(num_samps, at)
        gpu_window = cp.asnumpy(cusignal.windows.chebwin(num_samps, at))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_cosine(self, num_samps):
        cpu_window = signal.windows.cosine(num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.cosine(num_samps))
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("num_samps", [2 ** 15])
    @pytest.mark.parametrize("tau", [1.5, 3.0])
    def test_exponential(self, num_samps, tau):
        cpu_window = signal.windows.exponential(num_samps, tau=tau)
        gpu_window = cp.asnumpy(
            cusignal.windows.exponential(num_samps, tau=tau)
        )
        assert array_equal(cpu_window, gpu_window)

    @pytest.mark.parametrize("window", ["triang", "boxcar", "nuttall"])
    @pytest.mark.parametrize("num_samps", [2 ** 15])
    def test_get_window(self, window, num_samps):
        cpu_window = signal.windows.get_window(window, num_samps)
        gpu_window = cp.asnumpy(cusignal.windows.get_window(window, num_samps))
        assert array_equal(cpu_window, gpu_window)
