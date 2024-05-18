Benchmarks with tag 'apps':
===========================

| Benchmark      | benchmark | benchmark_jit          |
|----------------|:---------:|:----------------------:|
| docutils       | 7.65 sec  | 7.13 sec: 1.07x faster |
| Geometric mean | (ref)     | 1.01x faster           |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | benchmark | benchmark_jit          |
|----------------|:---------:|:----------------------:|
| tomli_loads    | 6.75 sec  | 6.71 sec: 1.01x faster |
| Geometric mean | (ref)     | 1.00x faster           |

Benchmark hidden because not significant (13): json_dumps, json_loads, pickle, pickle_dict, pickle_list, pickle_pure_python, unpickle, unpickle_list, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark               | benchmark | benchmark_jit          |
|-------------------------|:---------:|:----------------------:|
| aiohttp                 | 2.78 ms   | 2.75 ms: 1.01x faster  |
| asyncio_tcp             | 1.78 sec  | 1.76 sec: 1.01x faster |
| crypto_pyaes            | 281 ms    | 272 ms: 1.04x faster   |
| docutils                | 7.65 sec  | 7.13 sec: 1.07x faster |
| fannkuch                | 1.11 sec  | 1.10 sec: 1.01x faster |
| flaskblogging           | 8.67 ms   | 8.75 ms: 1.01x slower  |
| create_gc_cycles        | 3.10 ms   | 3.05 ms: 1.02x faster  |
| gc_traversal            | 7.43 ms   | 7.33 ms: 1.01x faster  |
| gunicorn                | 2.78 ms   | 2.74 ms: 1.02x faster  |
| logging_format          | 23.8 us   | 23.4 us: 1.02x faster  |
| mdp                     | 7.03 sec  | 6.99 sec: 1.01x faster |
| mypy2                   | 2.03 sec  | 2.02 sec: 1.01x faster |
| pycparser               | 3.61 sec  | 3.58 sec: 1.01x faster |
| scimark_fft             | 968 ms    | 957 ms: 1.01x faster   |
| scimark_sparse_mat_mult | 12.8 ms   | 12.5 ms: 1.02x faster  |
| sqlite_synth            | 5.29 us   | 5.35 us: 1.01x slower  |
| sympy_str               | 792 ms    | 784 ms: 1.01x faster   |
| tomli_loads             | 6.75 sec  | 6.71 sec: 1.01x faster |
| Geometric mean          | (ref)     | 1.00x faster           |

Benchmark hidden because not significant (82): 2to3, async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, asyncio_tcp_ssl, asyncio_websockets, chameleon, chaos, comprehensions, bench_mp_pool, bench_thread_pool, coroutines, coverage, dask, deepcopy, deepcopy_reduce, deepcopy_memo, deltablue, django_template, dulwich_log, float, generators, genshi_text, genshi_xml, go, hexiom, html5lib, json, json_dumps, json_loads, logging_silent, logging_simple, mako, meteor_contest, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_safe_repr, pprint_pformat, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_lu, scimark_monte_carlo, scimark_sor, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_parse, sqlglot_transpile, sqlglot_optimize, sqlglot_normalize, sympy_expand, sympy_integrate, sympy_sum, telco, thrift, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process
