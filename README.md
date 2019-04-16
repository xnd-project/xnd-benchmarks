# XND compared with NumPy

## How to run these benchmarks
Get the Anaconda or Miniconda distribution, install `asv` in your environment,
`cd` into the `asv directory`, and type `asv run`. That's it!

## The results

This benchmark represents the time to access arrays in the form `x[a][b][c]`,
where `a`, `b` and `c` are integers. `dim` is a tuple with the first dimension
representing the number of dimensions, and the second, the number of dimensions
indexed over. So if `dim[1] < dim[0]`, then we are accessing a sub-array. Size
represents the approximate number of elements in the array.

```
[ 66.67%] ··· benchmarks.DataAccessSuite.time_access_chained                  ok
[ 66.67%] ··· ========= ======== ============= =============
              --                            module
              ------------------ ---------------------------
                 size     dim         xnd            np
              ========= ======== ============= =============
                  1      (1, 1)     943±20ns      839±20ns
                  1      (2, 1)     933±20ns      955±40ns
                  1      (2, 2)   1.19±0.06μs   1.06±0.02μs
                  1      (3, 1)     921±30ns      938±3ns
                  1      (3, 2)   1.16±0.05μs   1.13±0.01μs
                  1      (3, 3)   1.35±0.04μs   1.28±0.03μs
                  10     (1, 1)     932±10ns      860±30ns
                  10     (2, 1)     938±30ns      896±3ns
                  10     (2, 2)   1.10±0.01μs   1.04±0.01μs
                  10     (3, 1)     896±8ns       926±20ns
                  10     (3, 2)   1.19±0.01μs   1.11±0.01μs
                  10     (3, 3)   1.34±0.03μs   1.24±0.01μs
                 100     (1, 1)     894±7ns       898±60ns
                 100     (2, 1)     938±30ns     951±100ns
                 100     (2, 2)     1.19±0μs    1.07±0.05μs
                 100     (3, 1)     920±20ns      880±8ns
                 100     (3, 2)   1.16±0.02μs   1.11±0.03μs
                 100     (3, 3)   1.40±0.01μs   1.26±0.02μs
                 1000    (1, 1)     901±30ns      849±30ns
                 1000    (2, 1)     940±30ns      936±40ns
                 1000    (2, 2)   1.18±0.03μs   1.10±0.05μs
                 1000    (3, 1)     918±20ns      936±20ns
                 1000    (3, 2)   1.18±0.04μs     1.11±0μs
                 1000    (3, 3)   1.38±0.03μs   1.27±0.04μs
                10000    (1, 1)     918±10ns      838±20ns
                10000    (2, 1)     956±20ns      906±20ns
                10000    (2, 2)   1.18±0.03μs   1.08±0.02μs
                10000    (3, 1)     941±10ns      931±10ns
                10000    (3, 2)   1.12±0.02μs   1.14±0.05μs
                10000    (3, 3)   1.39±0.01μs   1.29±0.01μs
                100000   (1, 1)     966±80ns      857±10ns
                100000   (2, 1)     933±5ns       926±20ns
                100000   (2, 2)   1.14±0.04μs   1.08±0.02μs
                100000   (3, 1)     944±20ns      938±30ns
                100000   (3, 2)   1.11±0.01μs   1.15±0.03μs
                100000   (3, 3)   1.42±0.01μs   1.30±0.04μs
               1000000   (1, 1)     969±20ns      879±40ns
               1000000   (2, 1)     959±8ns       909±10ns
               1000000   (2, 2)   1.14±0.01μs   1.08±0.02μs
               1000000   (3, 1)     941±10ns      937±4ns
               1000000   (3, 2)   1.14±0.03μs   1.14±0.01μs
               1000000   (3, 3)   1.39±0.01μs   1.33±0.01μs
              ========= ======== ============= =============
```

This benchmark represents the time to access arrays in the form `x[a, b, c]`, with
the parameters being the same as described above.

```
[ 83.33%] ··· benchmarks.DataAccessSuite.time_access_tuple                    ok
[ 83.33%] ··· ========= ======== ========== ==========
              --                         module
              ------------------ ---------------------
                 size     dim       xnd         np
              ========= ======== ========== ==========
                  1      (1, 1)   601±40ns   527±20ns
                  1      (2, 1)   608±10ns   602±10ns
                  1      (2, 2)   683±8ns    605±9ns
                  1      (3, 1)   619±20ns   607±2ns
                  1      (3, 2)   695±10ns   687±9ns
                  1      (3, 3)   728±20ns   629±20ns
                  10     (1, 1)   600±7ns    535±10ns
                  10     (2, 1)   615±20ns   606±2ns
                  10     (2, 2)   665±20ns   596±20ns
                  10     (3, 1)   629±7ns    611±20ns
                  10     (3, 2)   699±3ns    685±10ns
                  10     (3, 3)   723±6ns    643±7ns
                 100     (1, 1)   610±4ns    549±10ns
                 100     (2, 1)   623±10ns   613±30ns
                 100     (2, 2)   688±9ns    596±2ns
                 100     (3, 1)   646±9ns    614±10ns
                 100     (3, 2)   702±20ns   676±9ns
                 100     (3, 3)   744±9ns    631±30ns
                 1000    (1, 1)   595±20ns   532±20ns
                 1000    (2, 1)   622±5ns    602±30ns
                 1000    (2, 2)   691±80ns   629±9ns
                 1000    (3, 1)   642±7ns    627±6ns
                 1000    (3, 2)   709±20ns   693±30ns
                 1000    (3, 3)   737±20ns   649±10ns
                10000    (1, 1)   615±10ns   541±7ns
                10000    (2, 1)   631±20ns   592±10ns
                10000    (2, 2)   701±40ns   616±20ns
                10000    (3, 1)   619±6ns    628±30ns
                10000    (3, 2)   695±20ns   679±20ns
                10000    (3, 3)   738±9ns    654±5ns
                100000   (1, 1)   637±20ns   544±10ns
                100000   (2, 1)   624±10ns   599±10ns
                100000   (2, 2)   702±20ns   622±9ns
                100000   (3, 1)   667±20ns   619±20ns
                100000   (3, 2)   702±20ns   678±10ns
                100000   (3, 3)   715±20ns   633±5ns
               1000000   (1, 1)   615±8ns    543±6ns
               1000000   (2, 1)   617±2ns    604±5ns
               1000000   (2, 2)   689±7ns    615±10ns
               1000000   (3, 1)   630±10ns   623±2ns
               1000000   (3, 2)   711±9ns    685±10ns
               1000000   (3, 3)   740±10ns   639±10ns
              ========= ======== ========== ==========
```

This benchmark compares the type inference and array construction speeds. `full` is
only accessible in XND, and means that full type information is provided, including
the shape. `partial` means just the data type is provided, and `none` means no type
information is provided. The `tuple` datatype constructs an array from a tuple,
representing the values in a struct.

```
[100.00%] ··· benchmarks.DataConversionSuite.time_create                      ok
[100.00%] ··· ========= ========= =========== ============= =============
              --                                         module
              ------------------------------- ---------------------------
                 size     dtype    type_info       xnd            np
              ========= ========= =========== ============= =============
                  1      float64      full      5.06±0.2μs       n/a
                  1      float64    partial     10.0±0.4μs   2.28±0.02μs
                  1      float64      none      7.97±0.1μs    1.47±0.1μs
                  1       int64       full      4.97±0.1μs       n/a
                  1       int64     partial     10.1±0.2μs   2.36±0.07μs
                  1       int64       none      7.67±0.3μs    1.48±0.1μs
                  1       tuple       full      7.22±0.5μs       n/a
                  1       tuple     partial     12.3±0.2μs   1.90±0.03μs
                  1       tuple       none     8.83±0.07μs    3.20±0.2μs
                  10     float64      full     5.65±0.03μs       n/a
                  10     float64    partial     11.5±0.2μs   2.83±0.09μs
                  10     float64      none      8.49±0.1μs   1.95±0.07μs
                  10      int64       full      5.38±0.1μs       n/a
                  10      int64     partial     10.6±0.2μs   3.18±0.07μs
                  10      int64       none      8.39±0.2μs   2.31±0.01μs
                  10      tuple       full     8.86±0.03μs       n/a
                  10      tuple     partial     14.6±0.3μs   4.37±0.02μs
                  10      tuple       none      12.3±0.6μs    14.2±0.5μs
                 100     float64      full     7.94±0.07μs       n/a
                 100     float64    partial     15.3±0.1μs   7.14±0.06μs
                 100     float64      none       14.0±1μs     6.10±0.1μs
                 100      int64       full     7.78±0.08μs       n/a
                 100      int64     partial     15.5±0.2μs    11.0±0.3μs
                 100      int64       none      14.0±0.7μs    10.2±0.1μs
                 100      tuple       full      28.7±0.8μs       n/a
                 100      tuple     partial      36.3±1μs     28.7±0.4μs
                 100      tuple       none      36.4±0.4μs     125±3μs
                 1000    float64      full       33.0±3μs        n/a
                 1000    float64    partial     52.9±0.6μs     49.3±2μs
                 1000    float64      none       52.3±2μs     47.4±0.6μs
                 1000     int64       full      27.8±0.2μs       n/a
                 1000     int64     partial      46.2±1μs      86.9±2μs
                 1000     int64       none       54.5±3μs      85.8±2μs
                 1000     tuple       full       219±2μs         n/a
                 1000     tuple     partial      241±10μs      256±6μs
                 1000     tuple       none      256±0.3μs    1.13±0.06ms
                10000    float64      full       269±3μs         n/a
                10000    float64    partial      387±10μs      446±20μs
                10000    float64      none       392±2μs       454±20μs
                10000     int64       full       239±10μs        n/a
                10000     int64     partial      342±6μs       865±8μs
                10000     int64       none       445±6μs       861±20μs
                10000     tuple       full      2.07±0.2ms       n/a
                10000     tuple     partial    2.23±0.02ms   2.52±0.07ms
                10000     tuple       none     2.48±0.02ms    12.1±0.2ms
                100000   float64      full     2.77±0.03ms       n/a
                100000   float64    partial    3.77±0.04ms    4.72±0.1ms
                100000   float64      none      4.08±0.2ms    4.78±0.3ms
                100000    int64       full     2.31±0.08ms       n/a
                100000    int64     partial     3.53±0.1ms    8.64±0.1ms
                100000    int64       none     4.66±0.07ms   8.71±0.03ms
                100000    tuple       full      21.2±0.1ms       n/a
                100000    tuple     partial     22.1±0.1ms    26.0±0.5ms
                100000    tuple       none      25.7±0.3ms    117±0.7ms
               1000000   float64      full      27.6±0.9ms       n/a
               1000000   float64    partial     42.4±0.5ms     46.3±1ms
               1000000   float64      none      43.9±0.6ms    47.5±0.4ms
               1000000    int64       full      23.3±0.8ms       n/a
               1000000    int64     partial     38.1±0.6ms     87.3±1ms
               1000000    int64       none      48.8±0.8ms    85.8±0.8ms
               1000000    tuple       full       206±2ms         n/a
               1000000    tuple     partial      221±3ms       256±4ms
               1000000    tuple       none       256±3ms       1.17±0s
              ========= ========= =========== ============= =============
```
