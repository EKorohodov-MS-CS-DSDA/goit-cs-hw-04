# Time results

## For Original text

Multithread
```
Process 3572: {'models': 11, 'approaches': 1, 'mechanisms': 0}
Process 3572: {'models': 2, 'approaches': 14, 'mechanisms': 1}
Process 3572: {'models': 0, 'approaches': 0, 'mechanisms': 10}
[dict_items([('models', 13)]),
 dict_items([('approaches', 15)]),
 dict_items([('mechanisms', 11)])]
Time total: 0.001999378204345703
```

Multiprocess
```
Process 6700: {'models': 11, 'approaches': 1, 'mechanisms': 0}
Process 10968: {'models': 2, 'approaches': 14, 'mechanisms': 1}
Process 6912: {'models': 0, 'approaches': 0, 'mechanisms': 10} 
[[('models', 13)], [('approaches', 15)], [('mechanisms', 11)]]
Time total: 0.27334117889404297
```

## For x2048 scaled text
Multithread
```
Process 15352: {'models': 22528, 'approaches': 2048, 'mechanisms': 0}
Process 15352: {'models': 0, 'approaches': 0, 'mechanisms': 20480}
Process 15352: {'models': 4096, 'approaches': 28672, 'mechanisms': 2048}
[dict_items([('models', 26624)]),
 dict_items([('approaches', 30720)]),
 dict_items([('mechanisms', 22528)])]
Time total: 1.2077641487121582
```

Multiprocess
```
Process 3340: {'models': 0, 'approaches': 0, 'mechanisms': 20480}
Process 5632: {'models': 22528, 'approaches': 2048, 'mechanisms': 0}
Process 18200: {'models': 4096, 'approaches': 28672, 'mechanisms': 2048}
[[('models', 26624)], [('approaches', 30720)], [('mechanisms', 22528)]]
Time total: 1.117440938949585
```

## For x4096 scaled text

Multithread
```
Process 8548: {'models': 45056, 'approaches': 4096, 'mechanisms': 0}
Process 8548: {'models': 0, 'approaches': 0, 'mechanisms': 40960}
Process 8548: {'models': 8192, 'approaches': 57344, 'mechanisms': 4096}
[dict_items([('models', 53248)]),
 dict_items([('approaches', 61440)]),
 dict_items([('mechanisms', 45056)])]
Time total: 2.627628803253174
```

Multiprocess
```
Process 18316: {'models': 0, 'approaches': 0, 'mechanisms': 40960}
Process 1812: {'models': 45056, 'approaches': 4096, 'mechanisms': 0}
Process 2392: {'models': 8192, 'approaches': 57344, 'mechanisms': 4096}
[[('models', 53248)], [('approaches', 61440)], [('mechanisms', 45056)]]
Time total: 2.0036017894744873
```
