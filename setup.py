#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import subprocess

from setuptools import setup, Extension


version = "0.19.0-dev"


def pkg_config(package, option):
    try:
        output = subprocess.check_output(
            ["pkg-config", option, package],
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    return output.split()


def pkg_config_extension_args(package):
    pkg_compile_args = pkg_config(package, "--cflags")
    link_args = pkg_config(package, "--libs")
    if not pkg_compile_args and not link_args:
        return {
            "extra_compile_args": ["-std=c++11"],
            "libraries": ["csdr", "fftw3f"],
        }
    return {
        "extra_compile_args": ["-std=c++11"] + pkg_compile_args,
        "extra_link_args": link_args,
    }

setup(
    name="pycsdr",
    version=version,
    packages=["pycsdr"],

    package_data={
        "pycsdr": ["**.pyi", "**.py"],
    },

    headers=[
        "src/pycsdr.hpp",
        "src/reader.hpp",
        "src/writer.hpp",
        "src/source.hpp",
        "src/sink.hpp",
        "src/module.hpp",
        "src/buffer.hpp",
        "src/bufferreader.hpp",
    ],

    ext_modules=[
        Extension(
            name="pycsdr.modules",
            sources=[
                "src/pycsdr.cpp",
                "src/writer.cpp",
                "src/reader.cpp",
                "src/sink.cpp",
                "src/source.cpp",
                "src/buffer.cpp",
                "src/bufferreader.cpp",
                "src/tcpsource.cpp",
                "src/types.cpp",
                "src/module.cpp",
                "src/fft.cpp",
                "src/logpower.cpp",
                "src/logaveragepower.cpp",
                "src/fftswap.cpp",
                "src/fftadpcm.cpp",
                "src/firdecimate.cpp",
                "src/bandpass.cpp",
                "src/shift.cpp",
                "src/convert.cpp",
                "src/squelch.cpp",
                "src/fractionaldecimator.cpp",
                "src/fmdemod.cpp",
                "src/limit.cpp",
                "src/nfmdeemphasis.cpp",
                "src/wfmdeemphasis.cpp",
                "src/agc.cpp",
                "src/amdemod.cpp",
                "src/dcblock.cpp",
                "src/realpart.cpp",
                "src/audioresampler.cpp",
                "src/adpcmencoder.cpp",
                "src/downmix.cpp",
                "src/gain.cpp",
                "src/timingrecovery.cpp",
                "src/dbpskdecoder.cpp",
                "src/varicodedecoder.cpp",
                "src/phasedemod.cpp",
                "src/rtty.cpp",
                "src/baudot.cpp",
                "src/lowpass.cpp",
                "src/exec.cpp",
                "src/throttle.cpp",
            ],
            language="c++",
            include_dirs=["src"],
            define_macros=[("VERSION", '"{}"'.format(version))],
            **pkg_config_extension_args("csdr"),
        )
    ],
)
