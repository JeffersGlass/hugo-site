Having caught up with main, here's some stat counts and pyperformance analysis, exploring which subsets of superinstructions might be most valuable. For the moment, this incorporates both "format compatible" superinstructions that don't have overlapping oparg/operand/target, as well as incompatible ones that have overlap.

These are the top 500 Uop pairs when running pyperformance, as of where main was last night:

<details>
<summary>Pair counts for top 500 uop pairs</summary>


Pairs of specialized operations that deoptimize and are then followed by
the corresponding unspecialized instruction are not counted as pairs.

<table>
<thead>
<tr>
<th align="left">Pair</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _SET_IP</td>
<td align="right">4,918,363,112</td>
<td align="right">3.9%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_FALSE_POP</td>
<td align="right">2,969,434,496</td>
<td align="right">2.4%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _CHECK_VALIDITY</td>
<td align="right">2,264,639,698</td>
<td align="right">1.8%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_SET_IP _GUARD_BOTH_INT</td>
<td align="right">2,191,103,868</td>
<td align="right">1.7%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _GUARD_TYPE_VERSION</td>
<td align="right">1,459,822,326</td>
<td align="right">1.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _BINARY_OP_ADD_INT</td>
<td align="right">1,423,704,735</td>
<td align="right">1.1%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP _CHECK_VALIDITY</td>
<td align="right">1,420,911,788</td>
<td align="right">1.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_7</td>
<td align="right">1,399,351,760</td>
<td align="right">1.1%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR _CHECK_VALIDITY</td>
<td align="right">1,355,624,988</td>
<td align="right">1.1%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,353,346,729</td>
<td align="right">1.1%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP _CHECK_VALIDITY</td>
<td align="right">1,337,942,123</td>
<td align="right">1.1%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_SET_IP _GUARD_TYPE_VERSION</td>
<td align="right">1,335,297,273</td>
<td align="right">1.1%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,304,807,114</td>
<td align="right">1.0%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES _LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">1,300,440,674</td>
<td align="right">1.0%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CONTAINS_OP</td>
<td align="right">1,285,270,275</td>
<td align="right">1.0%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _SET_IP</td>
<td align="right">1,216,476,888</td>
<td align="right">1.0%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_0</td>
<td align="right">1,093,152,233</td>
<td align="right">0.9%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _SET_IP</td>
<td align="right">1,014,034,280</td>
<td align="right">0.8%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _LOAD_FAST_1</td>
<td align="right">988,738,960</td>
<td align="right">0.8%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_1</td>
<td align="right">952,849,438</td>
<td align="right">0.8%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _ITER_CHECK_LIST</td>
<td align="right">917,814,385</td>
<td align="right">0.7%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">904,887,014</td>
<td align="right">0.7%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _BINARY_SUBSCR_STR_INT</td>
<td align="right">881,863,700</td>
<td align="right">0.7%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST _GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">874,993,105</td>
<td align="right">0.7%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _STORE_FAST_1</td>
<td align="right">857,669,140</td>
<td align="right">0.7%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR _CHECK_VALIDITY</td>
<td align="right">848,787,380</td>
<td align="right">0.7%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _SET_IP</td>
<td align="right">846,004,624</td>
<td align="right">0.7%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_FALSE_POP</td>
<td align="right">830,506,949</td>
<td align="right">0.7%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS _CHECK_STACK_SPACE</td>
<td align="right">822,036,631</td>
<td align="right">0.7%</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET _PUSH_FRAME</td>
<td align="right">822,020,431</td>
<td align="right">0.7%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME _CHECK_VALIDITY</td>
<td align="right">821,630,772</td>
<td align="right">0.7%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _RESUME_CHECK</td>
<td align="right">813,263,876</td>
<td align="right">0.6%</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _STORE_FAST</td>
<td align="right">810,767,040</td>
<td align="right">0.6%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _SET_IP</td>
<td align="right">807,454,833</td>
<td align="right">0.6%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_1</td>
<td align="right">746,213,560</td>
<td align="right">0.6%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _TO_BOOL_BOOL</td>
<td align="right">727,644,702</td>
<td align="right">0.6%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST _ITER_NEXT_LIST</td>
<td align="right">727,407,997</td>
<td align="right">0.6%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST _CHECK_VALIDITY</td>
<td align="right">714,251,953</td>
<td align="right">0.6%</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_FAST</td>
<td align="right">713,623,873</td>
<td align="right">0.6%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">_CHECK_GLOBALS _CHECK_BUILTINS</td>
<td align="right">711,616,736</td>
<td align="right">0.6%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_TRUE_POP</td>
<td align="right">705,646,254</td>
<td align="right">0.6%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE _COMPARE_OP_STR</td>
<td align="right">695,452,528</td>
<td align="right">0.6%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_SET_IP _GUARD_BOTH_UNICODE</td>
<td align="right">694,580,668</td>
<td align="right">0.6%</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">694,400,296</td>
<td align="right">0.6%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">686,152,960</td>
<td align="right">0.5%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _LOAD_FAST_7</td>
<td align="right">685,391,500</td>
<td align="right">0.5%</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_FAST_3</td>
<td align="right">678,857,760</td>
<td align="right">0.5%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT _STORE_FAST_7</td>
<td align="right">674,395,140</td>
<td align="right">0.5%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _JUMP_TO_TOP</td>
<td align="right">663,656,340</td>
<td align="right">0.5%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _COMPARE_OP_STR</td>
<td align="right">660,496,080</td>
<td align="right">0.5%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_SUBSCR</td>
<td align="right">655,631,060</td>
<td align="right">0.5%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _SET_IP</td>
<td align="right">650,471,872</td>
<td align="right">0.5%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_CONST_INLINE_BORROW</td>
<td align="right">638,677,160</td>
<td align="right">0.5%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR _CHECK_VALIDITY</td>
<td align="right">632,782,284</td>
<td align="right">0.5%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST</td>
<td align="right">631,359,031</td>
<td align="right">0.5%</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">601,867,358</td>
<td align="right">0.5%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT _GUARD_KEYS_VERSION</td>
<td align="right">601,865,498</td>
<td align="right">0.5%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_5</td>
<td align="right">595,916,760</td>
<td align="right">0.5%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _SET_IP</td>
<td align="right">580,879,838</td>
<td align="right">0.5%</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _SET_IP</td>
<td align="right">578,566,486</td>
<td align="right">0.5%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">_SET_IP _CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">571,568,739</td>
<td align="right">0.5%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION _LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">554,428,258</td>
<td align="right">0.4%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _COMPARE_OP_INT</td>
<td align="right">552,599,400</td>
<td align="right">0.4%</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">547,321,100</td>
<td align="right">0.4%</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT _CHECK_VALIDITY</td>
<td align="right">546,886,480</td>
<td align="right">0.4%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_TRUE_POP</td>
<td align="right">531,008,516</td>
<td align="right">0.4%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST</td>
<td align="right">523,929,242</td>
<td align="right">0.4%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_CONST_INLINE_BORROW</td>
<td align="right">522,579,909</td>
<td align="right">0.4%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST</td>
<td align="right">522,159,679</td>
<td align="right">0.4%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_CONST_INLINE_BORROW</td>
<td align="right">517,421,780</td>
<td align="right">0.4%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _EXIT_TRACE</td>
<td align="right">512,905,025</td>
<td align="right">0.4%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE _GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">512,616,412</td>
<td align="right">0.4%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_SET_IP _ITER_CHECK_RANGE</td>
<td align="right">497,802,170</td>
<td align="right">0.4%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_ATTR</td>
<td align="right">497,569,794</td>
<td align="right">0.4%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE _ITER_NEXT_RANGE</td>
<td align="right">487,463,800</td>
<td align="right">0.4%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE _CHECK_VALIDITY</td>
<td align="right">486,047,800</td>
<td align="right">0.4%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST</td>
<td align="right">464,047,634</td>
<td align="right">0.4%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES _CHECK_VALIDITY</td>
<td align="right">463,541,726</td>
<td align="right">0.4%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">453,191,279</td>
<td align="right">0.4%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP</td>
<td align="right">449,837,780</td>
<td align="right">0.4%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_SLOT_0</td>
<td align="right">444,413,782</td>
<td align="right">0.4%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_FAST_0</td>
<td align="right">425,106,151</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _SET_IP</td>
<td align="right">416,290,640</td>
<td align="right">0.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">405,386,040</td>
<td align="right">0.3%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">403,364,660</td>
<td align="right">0.3%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP_ADD_INT</td>
<td align="right">382,082,580</td>
<td align="right">0.3%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_2</td>
<td align="right">381,757,711</td>
<td align="right">0.3%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O _CHECK_VALIDITY</td>
<td align="right">380,153,457</td>
<td align="right">0.3%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_4</td>
<td align="right">372,227,783</td>
<td align="right">0.3%</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_O</td>
<td align="right">365,069,977</td>
<td align="right">0.3%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">_CHECK_BUILTINS _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">356,017,693</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _SET_IP</td>
<td align="right">349,455,207</td>
<td align="right">0.3%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _ITER_CHECK_TUPLE</td>
<td align="right">340,832,212</td>
<td align="right">0.3%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _LOAD_ATTR</td>
<td align="right">336,466,159</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _SET_IP</td>
<td align="right">325,421,257</td>
<td align="right">0.3%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_SWAP _SET_IP</td>
<td align="right">319,885,628</td>
<td align="right">0.3%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_1</td>
<td align="right">315,916,373</td>
<td align="right">0.3%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST_3</td>
<td align="right">296,105,320</td>
<td align="right">0.2%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_DEREF</td>
<td align="right">292,326,540</td>
<td align="right">0.2%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE _GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">288,779,632</td>
<td align="right">0.2%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _TO_BOOL_BOOL</td>
<td align="right">286,918,299</td>
<td align="right">0.2%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF _CHECK_VALIDITY</td>
<td align="right">280,070,820</td>
<td align="right">0.2%</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_6</td>
<td align="right">268,077,620</td>
<td align="right">0.2%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0 _SET_IP</td>
<td align="right">267,796,778</td>
<td align="right">0.2%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_0</td>
<td align="right">266,956,143</td>
<td align="right">0.2%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE _INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">264,603,680</td>
<td align="right">0.2%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4 _SAVE_RETURN_OFFSET</td>
<td align="right">264,603,680</td>
<td align="right">0.2%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _JUMP_TO_TOP</td>
<td align="right">263,427,350</td>
<td align="right">0.2%</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_COPY _COPY</td>
<td align="right">258,412,840</td>
<td align="right">0.2%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_SWAP _SWAP</td>
<td align="right">258,412,840</td>
<td align="right">0.2%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">255,792,112</td>
<td align="right">0.2%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">_POP_FRAME _CHECK_VALIDITY</td>
<td align="right">255,171,976</td>
<td align="right">0.2%</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_6</td>
<td align="right">254,413,899</td>
<td align="right">0.2%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _GUARD_BOTH_FLOAT</td>
<td align="right">252,484,080</td>
<td align="right">0.2%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST</td>
<td align="right">251,462,700</td>
<td align="right">0.2%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _BINARY_SUBSCR</td>
<td align="right">250,658,220</td>
<td align="right">0.2%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _STORE_SUBSCR_LIST_INT</td>
<td align="right">247,430,260</td>
<td align="right">0.2%</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT _CHECK_VALIDITY</td>
<td align="right">247,379,380</td>
<td align="right">0.2%</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_0</td>
<td align="right">243,101,703</td>
<td align="right">0.2%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _BINARY_OP_ADD_FLOAT</td>
<td align="right">240,825,200</td>
<td align="right">0.2%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_3</td>
<td align="right">238,876,949</td>
<td align="right">0.2%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">237,010,581</td>
<td align="right">0.2%</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">_SET_IP _BUILD_TUPLE</td>
<td align="right">232,345,271</td>
<td align="right">0.2%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_5</td>
<td align="right">229,054,560</td>
<td align="right">0.2%</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">228,795,689</td>
<td align="right">0.2%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _POP_TOP</td>
<td align="right">227,671,252</td>
<td align="right">0.2%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE _INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">225,298,516</td>
<td align="right">0.2%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1 _SAVE_RETURN_OFFSET</td>
<td align="right">225,298,516</td>
<td align="right">0.2%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR _CHECK_VALIDITY</td>
<td align="right">221,273,340</td>
<td align="right">0.2%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE _INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">218,067,892</td>
<td align="right">0.2%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0 _SAVE_RETURN_OFFSET</td>
<td align="right">218,067,892</td>
<td align="right">0.2%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _IS_OP</td>
<td align="right">217,218,360</td>
<td align="right">0.2%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT _CHECK_VALIDITY</td>
<td align="right">216,180,698</td>
<td align="right">0.2%</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6 _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">216,000,120</td>
<td align="right">0.2%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _FOR_ITER_TIER_TWO</td>
<td align="right">215,603,443</td>
<td align="right">0.2%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _STORE_SUBSCR</td>
<td align="right">215,511,720</td>
<td align="right">0.2%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_0</td>
<td align="right">214,557,913</td>
<td align="right">0.2%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO _CHECK_VALIDITY</td>
<td align="right">204,795,848</td>
<td align="right">0.2%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_1</td>
<td align="right">204,726,360</td>
<td align="right">0.2%</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _GUARD_BOTH_FLOAT</td>
<td align="right">204,052,800</td>
<td align="right">0.2%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _GUARD_BOTH_FLOAT</td>
<td align="right">203,644,140</td>
<td align="right">0.2%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT _LOAD_FAST_2</td>
<td align="right">201,946,740</td>
<td align="right">0.2%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _CHECK_GLOBALS</td>
<td align="right">201,314,422</td>
<td align="right">0.2%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">201,253,609</td>
<td align="right">0.2%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _BINARY_OP_SUBTRACT_INT</td>
<td align="right">200,174,913</td>
<td align="right">0.2%</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_6</td>
<td align="right">198,824,423</td>
<td align="right">0.2%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _LOAD_FAST_0</td>
<td align="right">197,411,380</td>
<td align="right">0.2%</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">196,219,220</td>
<td align="right">0.2%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _STORE_FAST_2</td>
<td align="right">194,203,240</td>
<td align="right">0.2%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE _STORE_FAST_1</td>
<td align="right">194,139,940</td>
<td align="right">0.2%</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">_CHECK_BUILTINS _LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">193,745,723</td>
<td align="right">0.2%</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE _CHECK_VALIDITY</td>
<td align="right">191,310,751</td>
<td align="right">0.2%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE _ITER_NEXT_TUPLE</td>
<td align="right">190,236,760</td>
<td align="right">0.2%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _EXIT_TRACE</td>
<td align="right">190,022,880</td>
<td align="right">0.2%</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_3</td>
<td align="right">189,057,938</td>
<td align="right">0.2%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST_2</td>
<td align="right">187,786,740</td>
<td align="right">0.1%</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST _CHECK_VALIDITY</td>
<td align="right">187,657,180</td>
<td align="right">0.1%</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_IS_OP _GUARD_IS_TRUE_POP</td>
<td align="right">186,597,540</td>
<td align="right">0.1%</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">_CHECK_BUILTINS _LOAD_CONST_INLINE_BORROW</td>
<td align="right">184,752,800</td>
<td align="right">0.1%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">182,982,000</td>
<td align="right">0.1%</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _POP_FRAME</td>
<td align="right">182,906,060</td>
<td align="right">0.1%</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2 _SET_IP</td>
<td align="right">179,819,340</td>
<td align="right">0.1%</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">177,994,518</td>
<td align="right">0.1%</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _SET_IP</td>
<td align="right">176,186,875</td>
<td align="right">0.1%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE _CHECK_VALIDITY</td>
<td align="right">174,969,800</td>
<td align="right">0.1%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _JUMP_TO_TOP</td>
<td align="right">174,878,453</td>
<td align="right">0.1%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _BINARY_SUBSCR_LIST_INT</td>
<td align="right">173,368,153</td>
<td align="right">0.1%</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_FAST_1</td>
<td align="right">172,308,499</td>
<td align="right">0.1%</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_ISINSTANCE</td>
<td align="right">171,708,280</td>
<td align="right">0.1%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_CHECK_GLOBALS _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">168,917,039</td>
<td align="right">0.1%</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3 _LOAD_FAST_3</td>
<td align="right">168,515,841</td>
<td align="right">0.1%</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_FAST</td>
<td align="right">166,009,860</td>
<td align="right">0.1%</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _BUILD_LIST</td>
<td align="right">165,738,859</td>
<td align="right">0.1%</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _STORE_FAST</td>
<td align="right">164,171,320</td>
<td align="right">0.1%</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT _LOAD_CONST_INLINE_BORROW</td>
<td align="right">163,476,280</td>
<td align="right">0.1%</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">163,144,440</td>
<td align="right">0.1%</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _GUARD_TYPE_VERSION</td>
<td align="right">160,834,296</td>
<td align="right">0.1%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _TO_BOOL_BOOL</td>
<td align="right">160,445,300</td>
<td align="right">0.1%</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_6</td>
<td align="right">158,992,240</td>
<td align="right">0.1%</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS _CHECK_VALIDITY</td>
<td align="right">158,396,838</td>
<td align="right">0.1%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT _STORE_FAST</td>
<td align="right">158,126,100</td>
<td align="right">0.1%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _SET_IP</td>
<td align="right">156,425,215</td>
<td align="right">0.1%</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _LOAD_GLOBAL</td>
<td align="right">155,172,060</td>
<td align="right">0.1%</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL _CHECK_VALIDITY</td>
<td align="right">155,010,540</td>
<td align="right">0.1%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_CONST_INLINE_BORROW</td>
<td align="right">154,256,140</td>
<td align="right">0.1%</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">_COPY _BINARY_SUBSCR_LIST_INT</td>
<td align="right">152,903,800</td>
<td align="right">0.1%</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _GUARD_TYPE_VERSION</td>
<td align="right">152,447,720</td>
<td align="right">0.1%</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST_2</td>
<td align="right">150,140,840</td>
<td align="right">0.1%</td>
<td align="right">77.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6 _STORE_FAST_7</td>
<td align="right">144,966,539</td>
<td align="right">0.1%</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _CHECK_GLOBALS</td>
<td align="right">142,970,224</td>
<td align="right">0.1%</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5 _LOAD_FAST_5</td>
<td align="right">141,867,000</td>
<td align="right">0.1%</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_FAST</td>
<td align="right">141,031,600</td>
<td align="right">0.1%</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_3</td>
<td align="right">139,320,893</td>
<td align="right">0.1%</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL _LOAD_FAST_1</td>
<td align="right">134,694,560</td>
<td align="right">0.1%</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_CONST_INLINE</td>
<td align="right">133,342,480</td>
<td align="right">0.1%</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _CALL_TYPE_1</td>
<td align="right">132,000,260</td>
<td align="right">0.1%</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1 _STORE_FAST_5</td>
<td align="right">132,000,000</td>
<td align="right">0.1%</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">_COPY _SET_IP</td>
<td align="right">131,831,380</td>
<td align="right">0.1%</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL _CHECK_VALIDITY</td>
<td align="right">131,621,759</td>
<td align="right">0.1%</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4 _LOAD_FAST_4</td>
<td align="right">130,358,520</td>
<td align="right">0.1%</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _EXIT_TRACE</td>
<td align="right">129,538,213</td>
<td align="right">0.1%</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _STORE_FAST</td>
<td align="right">128,288,760</td>
<td align="right">0.1%</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5 _LOAD_FAST_3</td>
<td align="right">127,732,520</td>
<td align="right">0.1%</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _EXIT_TRACE</td>
<td align="right">127,027,900</td>
<td align="right">0.1%</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_FAST_0</td>
<td align="right">126,747,616</td>
<td align="right">0.1%</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">_CHECK_GLOBALS _LOAD_CONST_INLINE</td>
<td align="right">126,352,513</td>
<td align="right">0.1%</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT _GUARD_IS_TRUE_POP</td>
<td align="right">125,590,232</td>
<td align="right">0.1%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_4</td>
<td align="right">124,237,954</td>
<td align="right">0.1%</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _TO_BOOL_INT</td>
<td align="right">123,928,500</td>
<td align="right">0.1%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_LEN</td>
<td align="right">121,903,322</td>
<td align="right">0.1%</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT _SET_IP</td>
<td align="right">121,373,680</td>
<td align="right">0.1%</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST</td>
<td align="right">118,857,900</td>
<td align="right">0.1%</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST_5</td>
<td align="right">118,741,560</td>
<td align="right">0.1%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">118,390,080</td>
<td align="right">0.1%</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _POP_FRAME</td>
<td align="right">118,164,340</td>
<td align="right">0.1%</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5 _STORE_FAST_6</td>
<td align="right">117,718,590</td>
<td align="right">0.1%</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST_4</td>
<td align="right">117,389,920</td>
<td align="right">0.1%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _CHECK_GLOBALS</td>
<td align="right">116,743,660</td>
<td align="right">0.1%</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_SUBSCR_DICT</td>
<td align="right">116,503,380</td>
<td align="right">0.1%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_2</td>
<td align="right">115,268,052</td>
<td align="right">0.1%</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN _CHECK_VALIDITY</td>
<td align="right">113,575,439</td>
<td align="right">0.1%</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _GUARD_TYPE_VERSION</td>
<td align="right">111,886,724</td>
<td align="right">0.1%</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT _SWAP</td>
<td align="right">111,719,820</td>
<td align="right">0.1%</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _STORE_FAST</td>
<td align="right">110,395,580</td>
<td align="right">0.1%</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_4</td>
<td align="right">108,393,839</td>
<td align="right">0.1%</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_SET_IP _STORE_SLICE</td>
<td align="right">108,249,300</td>
<td align="right">0.1%</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE _CHECK_VALIDITY</td>
<td align="right">108,071,340</td>
<td align="right">0.1%</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _LOAD_CONST_INLINE_BORROW</td>
<td align="right">108,028,920</td>
<td align="right">0.1%</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _BINARY_OP_ADD_FLOAT</td>
<td align="right">106,167,460</td>
<td align="right">0.1%</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_7</td>
<td align="right">106,076,219</td>
<td align="right">0.1%</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP_MULTIPLY_INT</td>
<td align="right">106,059,360</td>
<td align="right">0.1%</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _LOAD_FAST_0</td>
<td align="right">105,776,580</td>
<td align="right">0.1%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _BUILD_SLICE</td>
<td align="right">104,807,000</td>
<td align="right">0.1%</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">104,807,000</td>
<td align="right">0.1%</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _CHECK_GLOBALS</td>
<td align="right">103,977,683</td>
<td align="right">0.1%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _UNPACK_SEQUENCE_TUPLE</td>
<td align="right">102,015,240</td>
<td align="right">0.1%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP _LOAD_FAST_0</td>
<td align="right">101,912,673</td>
<td align="right">0.1%</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_4</td>
<td align="right">101,748,360</td>
<td align="right">0.1%</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE _STORE_FAST_5</td>
<td align="right">101,269,140</td>
<td align="right">0.1%</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_CONST_INLINE_BORROW</td>
<td align="right">101,074,840</td>
<td align="right">0.1%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_BOTH_FLOAT</td>
<td align="right">100,770,780</td>
<td align="right">0.1%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _SET_IP</td>
<td align="right">98,382,771</td>
<td align="right">0.1%</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT _SET_IP</td>
<td align="right">98,036,040</td>
<td align="right">0.1%</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _LOAD_FAST</td>
<td align="right">97,939,980</td>
<td align="right">0.1%</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT _CHECK_VALIDITY</td>
<td align="right">96,378,220</td>
<td align="right">0.1%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0 _LOAD_FAST_0</td>
<td align="right">96,233,601</td>
<td align="right">0.1%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _PUSH_NULL</td>
<td align="right">96,107,180</td>
<td align="right">0.1%</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">_SET_IP _GET_ITER</td>
<td align="right">96,001,942</td>
<td align="right">0.1%</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _LIST_EXTEND</td>
<td align="right">95,871,519</td>
<td align="right">0.1%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _CALL_INTRINSIC_1</td>
<td align="right">95,527,357</td>
<td align="right">0.1%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1 _CHECK_VALIDITY</td>
<td align="right">95,527,357</td>
<td align="right">0.1%</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">95,527,357</td>
<td align="right">0.1%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST_1</td>
<td align="right">95,097,534</td>
<td align="right">0.1%</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4 _LOAD_FAST_1</td>
<td align="right">94,720,020</td>
<td align="right">0.1%</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _PUSH_NULL</td>
<td align="right">94,539,900</td>
<td align="right">0.1%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">_SET_IP _GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">0.1%</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT _CHECK_VALIDITY</td>
<td align="right">94,136,760</td>
<td align="right">0.1%</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _STORE_FAST_4</td>
<td align="right">94,057,860</td>
<td align="right">0.1%</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _TO_BOOL</td>
<td align="right">94,014,919</td>
<td align="right">0.1%</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _BINARY_OP</td>
<td align="right">91,962,588</td>
<td align="right">0.1%</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">90,886,532</td>
<td align="right">0.1%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT _CHECK_VALIDITY</td>
<td align="right">89,729,240</td>
<td align="right">0.1%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _STORE_SUBSCR_DICT</td>
<td align="right">89,352,720</td>
<td align="right">0.1%</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_COPY _TO_BOOL_BOOL</td>
<td align="right">88,503,260</td>
<td align="right">0.1%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND _JUMP_TO_TOP</td>
<td align="right">87,956,800</td>
<td align="right">0.1%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER _CHECK_VALIDITY</td>
<td align="right">87,952,440</td>
<td align="right">0.1%</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST</td>
<td align="right">86,627,840</td>
<td align="right">0.1%</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _COPY</td>
<td align="right">86,422,960</td>
<td align="right">0.1%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _EXIT_TRACE</td>
<td align="right">85,668,020</td>
<td align="right">0.1%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_5</td>
<td align="right">85,249,540</td>
<td align="right">0.1%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_0</td>
<td align="right">83,969,542</td>
<td align="right">0.1%</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _LOAD_FAST_3</td>
<td align="right">83,852,500</td>
<td align="right">0.1%</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _GUARD_BOTH_FLOAT</td>
<td align="right">83,571,960</td>
<td align="right">0.1%</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_0</td>
<td align="right">83,072,901</td>
<td align="right">0.1%</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP_SUBTRACT_INT</td>
<td align="right">82,654,660</td>
<td align="right">0.1%</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">_POP_FRAME _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">82,142,040</td>
<td align="right">0.1%</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2 _LOAD_FAST_2</td>
<td align="right">79,313,095</td>
<td align="right">0.1%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT _LOAD_FAST</td>
<td align="right">78,536,760</td>
<td align="right">0.1%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _SET_IP</td>
<td align="right">78,197,020</td>
<td align="right">0.1%</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE _GUARD_IS_FALSE_POP</td>
<td align="right">78,040,120</td>
<td align="right">0.1%</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">77,069,128</td>
<td align="right">0.1%</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _LOAD_FAST</td>
<td align="right">76,961,520</td>
<td align="right">0.1%</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _UNPACK_SEQUENCE_TUPLE</td>
<td align="right">76,396,220</td>
<td align="right">0.1%</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_2</td>
<td align="right">76,231,540</td>
<td align="right">0.1%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _SET_IP</td>
<td align="right">75,845,515</td>
<td align="right">0.1%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _GUARD_DORV_VALUES</td>
<td align="right">75,408,865</td>
<td align="right">0.1%</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES _STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">75,147,745</td>
<td align="right">0.1%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_FAST_2</td>
<td align="right">74,313,820</td>
<td align="right">0.1%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _TO_BOOL_NONE</td>
<td align="right">73,650,180</td>
<td align="right">0.1%</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_7</td>
<td align="right">73,601,700</td>
<td align="right">0.1%</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">73,537,098</td>
<td align="right">0.1%</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_FAST</td>
<td align="right">73,230,503</td>
<td align="right">0.1%</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE _STORE_FAST</td>
<td align="right">72,688,740</td>
<td align="right">0.1%</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT _STORE_FAST</td>
<td align="right">72,579,060</td>
<td align="right">0.1%</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _JUMP_TO_TOP</td>
<td align="right">72,541,965</td>
<td align="right">0.1%</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT _STORE_FAST</td>
<td align="right">72,535,680</td>
<td align="right">0.1%</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST_7</td>
<td align="right">72,521,740</td>
<td align="right">0.1%</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_FAST_0</td>
<td align="right">72,503,795</td>
<td align="right">0.1%</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0 _TO_BOOL_BOOL</td>
<td align="right">72,429,404</td>
<td align="right">0.1%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_SLICE</td>
<td align="right">72,209,260</td>
<td align="right">0.1%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _SET_IP</td>
<td align="right">72,111,240</td>
<td align="right">0.1%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _CHECK_GLOBALS</td>
<td align="right">72,079,620</td>
<td align="right">0.1%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_FAST_2</td>
<td align="right">72,078,820</td>
<td align="right">0.1%</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _LOAD_FAST_1</td>
<td align="right">71,839,797</td>
<td align="right">0.1%</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_1</td>
<td align="right">71,386,691</td>
<td align="right">0.1%</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">71,352,260</td>
<td align="right">0.1%</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3 _LOAD_FAST_2</td>
<td align="right">70,183,595</td>
<td align="right">0.1%</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_5</td>
<td align="right">69,998,500</td>
<td align="right">0.1%</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _EXIT_TRACE</td>
<td align="right">69,826,233</td>
<td align="right">0.1%</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _CHECK_GLOBALS</td>
<td align="right">69,437,306</td>
<td align="right">0.1%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_3</td>
<td align="right">68,845,620</td>
<td align="right">0.1%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _COPY</td>
<td align="right">68,408,220</td>
<td align="right">0.1%</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_FAST_1</td>
<td align="right">67,540,680</td>
<td align="right">0.1%</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE _CHECK_VALIDITY</td>
<td align="right">67,303,785</td>
<td align="right">0.1%</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE _INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">67,232,420</td>
<td align="right">0.1%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2 _SAVE_RETURN_OFFSET</td>
<td align="right">67,232,420</td>
<td align="right">0.1%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT _LOAD_FAST_1</td>
<td align="right">67,082,400</td>
<td align="right">0.1%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE _STORE_FAST_4</td>
<td align="right">65,577,800</td>
<td align="right">0.1%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_1</td>
<td align="right">65,312,380</td>
<td align="right">0.1%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP _CHECK_VALIDITY</td>
<td align="right">64,794,840</td>
<td align="right">0.1%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5 _LOAD_FAST_4</td>
<td align="right">64,511,140</td>
<td align="right">0.1%</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST_5</td>
<td align="right">64,089,340</td>
<td align="right">0.1%</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_FAST_2</td>
<td align="right">64,065,260</td>
<td align="right">0.1%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _LOAD_FAST_0</td>
<td align="right">63,772,400</td>
<td align="right">0.1%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _PUSH_NULL</td>
<td align="right">63,270,712</td>
<td align="right">0.1%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST_0</td>
<td align="right">63,116,280</td>
<td align="right">0.1%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _EXIT_TRACE</td>
<td align="right">62,407,760</td>
<td align="right">0.0%</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE _STORE_FAST</td>
<td align="right">62,321,660</td>
<td align="right">0.0%</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _LOAD_FAST_3</td>
<td align="right">61,960,540</td>
<td align="right">0.0%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_2</td>
<td align="right">61,511,887</td>
<td align="right">0.0%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_FAST_5</td>
<td align="right">61,445,780</td>
<td align="right">0.0%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT _STORE_FAST</td>
<td align="right">61,320,000</td>
<td align="right">0.0%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _LOAD_FAST</td>
<td align="right">61,112,480</td>
<td align="right">0.0%</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP _LOAD_FAST_1</td>
<td align="right">61,092,660</td>
<td align="right">0.0%</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _EXIT_TRACE</td>
<td align="right">61,017,393</td>
<td align="right">0.0%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _CHECK_ATTR_WITH_HINT</td>
<td align="right">60,898,980</td>
<td align="right">0.0%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT _LOAD_ATTR_WITH_HINT</td>
<td align="right">60,898,980</td>
<td align="right">0.0%</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _IS_OP</td>
<td align="right">60,799,660</td>
<td align="right">0.0%</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">60,360,368</td>
<td align="right">0.0%</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _PUSH_NULL</td>
<td align="right">59,852,400</td>
<td align="right">0.0%</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _PUSH_NULL</td>
<td align="right">59,793,536</td>
<td align="right">0.0%</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3 _JUMP_TO_TOP</td>
<td align="right">59,593,260</td>
<td align="right">0.0%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_CONST_INLINE</td>
<td align="right">59,522,820</td>
<td align="right">0.0%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT _LOAD_CONST_INLINE_BORROW</td>
<td align="right">59,219,700</td>
<td align="right">0.0%</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST_5</td>
<td align="right">58,850,220</td>
<td align="right">0.0%</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">58,591,914</td>
<td align="right">0.0%</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _LOAD_CONST_INLINE_BORROW</td>
<td align="right">58,533,300</td>
<td align="right">0.0%</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">_IS_OP _GUARD_IS_FALSE_POP</td>
<td align="right">57,810,240</td>
<td align="right">0.0%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_CONST_INLINE</td>
<td align="right">57,695,360</td>
<td align="right">0.0%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _EXIT_TRACE</td>
<td align="right">57,548,440</td>
<td align="right">0.0%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">57,501,900</td>
<td align="right">0.0%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _COPY</td>
<td align="right">57,340,408</td>
<td align="right">0.0%</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _STORE_ATTR_SLOT</td>
<td align="right">57,184,694</td>
<td align="right">0.0%</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">_COPY _GUARD_TYPE_VERSION</td>
<td align="right">57,039,148</td>
<td align="right">0.0%</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _LIST_APPEND</td>
<td align="right">55,780,722</td>
<td align="right">0.0%</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT _SWAP</td>
<td align="right">55,726,933</td>
<td align="right">0.0%</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT _SWAP</td>
<td align="right">55,700,820</td>
<td align="right">0.0%</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_FAST_1</td>
<td align="right">55,537,440</td>
<td align="right">0.0%</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">_SET_IP _COMPARE_OP</td>
<td align="right">55,478,220</td>
<td align="right">0.0%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4 _STORE_FAST_5</td>
<td align="right">55,409,260</td>
<td align="right">0.0%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _STORE_FAST</td>
<td align="right">55,344,460</td>
<td align="right">0.0%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4 _LOAD_FAST_3</td>
<td align="right">55,162,160</td>
<td align="right">0.0%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST_5</td>
<td align="right">54,943,620</td>
<td align="right">0.0%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_CONST_INLINE_BORROW</td>
<td align="right">54,463,943</td>
<td align="right">0.0%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_FAST_4</td>
<td align="right">54,448,360</td>
<td align="right">0.0%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">54,411,000</td>
<td align="right">0.0%</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _CHECK_GLOBALS</td>
<td align="right">54,384,500</td>
<td align="right">0.0%</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_FAST_4</td>
<td align="right">54,113,560</td>
<td align="right">0.0%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS _CHECK_VALIDITY</td>
<td align="right">54,091,120</td>
<td align="right">0.0%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">54,006,060</td>
<td align="right">0.0%</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _CONTAINS_OP</td>
<td align="right">53,520,308</td>
<td align="right">0.0%</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST</td>
<td align="right">52,934,660</td>
<td align="right">0.0%</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3 _CHECK_GLOBALS</td>
<td align="right">52,811,268</td>
<td align="right">0.0%</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE _STORE_FAST_4</td>
<td align="right">52,377,420</td>
<td align="right">0.0%</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">_CHECK_GLOBALS _LOAD_CONST_INLINE_BORROW</td>
<td align="right">51,414,923</td>
<td align="right">0.0%</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT _CHECK_VALIDITY</td>
<td align="right">51,138,194</td>
<td align="right">0.0%</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _BINARY_SUBSCR_LIST_INT</td>
<td align="right">51,002,440</td>
<td align="right">0.0%</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _SWAP</td>
<td align="right">50,433,900</td>
<td align="right">0.0%</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _PUSH_NULL</td>
<td align="right">49,650,140</td>
<td align="right">0.0%</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _CHECK_GLOBALS</td>
<td align="right">49,621,840</td>
<td align="right">0.0%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT _CHECK_VALIDITY</td>
<td align="right">49,181,760</td>
<td align="right">0.0%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_CONST_INLINE_BORROW</td>
<td align="right">48,178,520</td>
<td align="right">0.0%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _PUSH_NULL</td>
<td align="right">47,669,120</td>
<td align="right">0.0%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _JUMP_TO_TOP</td>
<td align="right">47,062,620</td>
<td align="right">0.0%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _LOAD_FAST_0</td>
<td align="right">47,005,920</td>
<td align="right">0.0%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE _CHECK_VALIDITY</td>
<td align="right">46,908,020</td>
<td align="right">0.0%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST_6</td>
<td align="right">46,478,220</td>
<td align="right">0.0%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_FAST_1</td>
<td align="right">46,176,120</td>
<td align="right">0.0%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP _LOAD_FAST</td>
<td align="right">45,819,900</td>
<td align="right">0.0%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST</td>
<td align="right">45,734,000</td>
<td align="right">0.0%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_FAST_4</td>
<td align="right">45,637,300</td>
<td align="right">0.0%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _LOAD_FAST_5</td>
<td align="right">45,420,360</td>
<td align="right">0.0%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _TO_BOOL_BOOL</td>
<td align="right">45,270,880</td>
<td align="right">0.0%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION _LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">45,256,000</td>
<td align="right">0.0%</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_FAST_2</td>
<td align="right">45,103,440</td>
<td align="right">0.0%</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _COPY</td>
<td align="right">44,631,180</td>
<td align="right">0.0%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_CONST_INLINE</td>
<td align="right">44,062,880</td>
<td align="right">0.0%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST _CHECK_VALIDITY</td>
<td align="right">43,878,174</td>
<td align="right">0.0%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST_2</td>
<td align="right">43,836,000</td>
<td align="right">0.0%</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _LOAD_FAST_0</td>
<td align="right">43,125,160</td>
<td align="right">0.0%</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2 _LOAD_FAST_0</td>
<td align="right">43,017,372</td>
<td align="right">0.0%</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _BINARY_SUBSCR_LIST_INT</td>
<td align="right">42,820,920</td>
<td align="right">0.0%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST_3</td>
<td align="right">42,483,314</td>
<td align="right">0.0%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST_7</td>
<td align="right">42,385,780</td>
<td align="right">0.0%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST</td>
<td align="right">42,334,620</td>
<td align="right">0.0%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _CALL_BUILTIN_FAST</td>
<td align="right">42,237,000</td>
<td align="right">0.0%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT _LOAD_FAST_0</td>
<td align="right">41,992,140</td>
<td align="right">0.0%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _POP_TOP</td>
<td align="right">41,590,740</td>
<td align="right">0.0%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">41,578,300</td>
<td align="right">0.0%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _TO_BOOL_BOOL</td>
<td align="right">41,380,800</td>
<td align="right">0.0%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _LOAD_FAST_1</td>
<td align="right">41,340,900</td>
<td align="right">0.0%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT _CHECK_VALIDITY</td>
<td align="right">40,939,500</td>
<td align="right">0.0%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _COMPARE_OP_FLOAT</td>
<td align="right">40,939,500</td>
<td align="right">0.0%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _EXIT_TRACE</td>
<td align="right">40,718,080</td>
<td align="right">0.0%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _GUARD_BOTH_FLOAT</td>
<td align="right">40,680,320</td>
<td align="right">0.0%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _LOAD_FAST</td>
<td align="right">40,521,420</td>
<td align="right">0.0%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_CONST_INLINE</td>
<td align="right">40,402,800</td>
<td align="right">0.0%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT _STORE_FAST_3</td>
<td align="right">40,248,000</td>
<td align="right">0.0%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _EXIT_TRACE</td>
<td align="right">40,229,840</td>
<td align="right">0.0%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_SET_IP _GUARD_BOTH_FLOAT</td>
<td align="right">39,838,320</td>
<td align="right">0.0%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5 _LOAD_FAST_2</td>
<td align="right">39,431,880</td>
<td align="right">0.0%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE _INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">39,272,600</td>
<td align="right">0.0%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3 _SAVE_RETURN_OFFSET</td>
<td align="right">39,272,600</td>
<td align="right">0.0%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP _JUMP_TO_TOP</td>
<td align="right">39,081,200</td>
<td align="right">0.0%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">38,471,400</td>
<td align="right">0.0%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _SWAP</td>
<td align="right">38,352,775</td>
<td align="right">0.0%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_CONST_INLINE</td>
<td align="right">38,146,880</td>
<td align="right">0.0%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">_SET_IP _LIST_APPEND</td>
<td align="right">38,067,840</td>
<td align="right">0.0%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR _CHECK_VALIDITY</td>
<td align="right">37,984,860</td>
<td align="right">0.0%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_FAST_3</td>
<td align="right">37,965,392</td>
<td align="right">0.0%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _COPY</td>
<td align="right">37,818,980</td>
<td align="right">0.0%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _TO_BOOL</td>
<td align="right">37,606,840</td>
<td align="right">0.0%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _BINARY_SUBSCR_LIST_INT</td>
<td align="right">37,438,980</td>
<td align="right">0.0%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_CONST_INLINE</td>
<td align="right">37,283,400</td>
<td align="right">0.0%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST _GUARD_IS_TRUE_POP</td>
<td align="right">36,948,837</td>
<td align="right">0.0%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4 _LOAD_FAST_0</td>
<td align="right">36,566,759</td>
<td align="right">0.0%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _POP_FRAME</td>
<td align="right">36,243,616</td>
<td align="right">0.0%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_IS_OP _EXIT_TRACE</td>
<td align="right">36,054,120</td>
<td align="right">0.0%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _STORE_FAST</td>
<td align="right">36,053,820</td>
<td align="right">0.0%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2 _CHECK_GLOBALS</td>
<td align="right">36,041,600</td>
<td align="right">0.0%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _STORE_ATTR</td>
<td align="right">36,004,520</td>
<td align="right">0.0%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_FAST_7</td>
<td align="right">35,712,623</td>
<td align="right">0.0%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _GUARD_BOTH_FLOAT</td>
<td align="right">35,412,900</td>
<td align="right">0.0%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">34,756,120</td>
<td align="right">0.0%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_FAST_4</td>
<td align="right">34,541,580</td>
<td align="right">0.0%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_2</td>
<td align="right">34,506,260</td>
<td align="right">0.0%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _POP_TOP</td>
<td align="right">33,666,054</td>
<td align="right">0.0%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _CHECK_GLOBALS</td>
<td align="right">33,180,720</td>
<td align="right">0.0%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_1</td>
<td align="right">32,642,240</td>
<td align="right">0.0%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_7</td>
<td align="right">32,375,190</td>
<td align="right">0.0%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_FAST_3</td>
<td align="right">32,094,300</td>
<td align="right">0.0%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST _STORE_FAST_4</td>
<td align="right">31,995,820</td>
<td align="right">0.0%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION _LOAD_GLOBAL_MODULE</td>
<td align="right">31,871,200</td>
<td align="right">0.0%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">31,641,900</td>
<td align="right">0.0%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">31,305,000</td>
<td align="right">0.0%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _BINARY_OP_MULTIPLY_INT</td>
<td align="right">31,291,980</td>
<td align="right">0.0%</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_FAST</td>
<td align="right">31,182,960</td>
<td align="right">0.0%</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_4</td>
<td align="right">31,088,960</td>
<td align="right">0.0%</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_CLASS</td>
<td align="right">30,828,122</td>
<td align="right">0.0%</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_STR_1</td>
<td align="right">30,760,980</td>
<td align="right">0.0%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _COPY</td>
<td align="right">30,660,000</td>
<td align="right">0.0%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _BUILD_TUPLE</td>
<td align="right">30,317,740</td>
<td align="right">0.0%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _UNARY_NOT</td>
<td align="right">29,833,560</td>
<td align="right">0.0%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST_5</td>
<td align="right">29,776,800</td>
<td align="right">0.0%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _STORE_FAST</td>
<td align="right">29,651,151</td>
<td align="right">0.0%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE _STORE_FAST</td>
<td align="right">29,418,900</td>
<td align="right">0.0%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _LOAD_FAST_6</td>
<td align="right">29,222,260</td>
<td align="right">0.0%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">28,551,240</td>
<td align="right">0.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _GUARD_TYPE_VERSION</td>
<td align="right">28,132,220</td>
<td align="right">0.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE _STORE_FAST_3</td>
<td align="right">28,094,900</td>
<td align="right">0.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP _BUILD_LIST</td>
<td align="right">27,589,661</td>
<td align="right">0.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_CONST_INLINE</td>
<td align="right">27,277,633</td>
<td align="right">0.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">27,139,181</td>
<td align="right">0.0%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _COPY</td>
<td align="right">27,075,060</td>
<td align="right">0.0%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _BINARY_SUBSCR_LIST_INT</td>
<td align="right">26,751,180</td>
<td align="right">0.0%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">26,593,640</td>
<td align="right">0.0%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_7</td>
<td align="right">26,591,859</td>
<td align="right">0.0%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">26,582,134</td>
<td align="right">0.0%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_CONST_INLINE</td>
<td align="right">26,531,280</td>
<td align="right">0.0%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0 _LOAD_FAST_0</td>
<td align="right">26,402,700</td>
<td align="right">0.0%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_3</td>
<td align="right">26,236,760</td>
<td align="right">0.0%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _COPY</td>
<td align="right">26,098,220</td>
<td align="right">0.0%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6 _LOAD_FAST_6</td>
<td align="right">25,801,900</td>
<td align="right">0.0%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS _INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">25,796,200</td>
<td align="right">0.0%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS _CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">25,796,200</td>
<td align="right">0.0%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_SET_IP _COMPARE_OP_INT</td>
<td align="right">25,592,080</td>
<td align="right">0.0%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1 _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">25,569,900</td>
<td align="right">0.0%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT _LOAD_FAST_1</td>
<td align="right">25,560,900</td>
<td align="right">0.0%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0 _STORE_FAST_3</td>
<td align="right">25,342,340</td>
<td align="right">0.0%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE _CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">25,327,400</td>
<td align="right">0.0%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL _CHECK_GLOBALS</td>
<td align="right">25,109,740</td>
<td align="right">0.0%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT _COPY</td>
<td align="right">25,016,660</td>
<td align="right">0.0%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_5</td>
<td align="right">24,924,960</td>
<td align="right">0.0%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _BINARY_SUBSCR_LIST_INT</td>
<td align="right">24,703,540</td>
<td align="right">0.0%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES _LOAD_FAST</td>
<td align="right">24,697,200</td>
<td align="right">0.0%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _LOAD_CONST_INLINE</td>
<td align="right">24,548,420</td>
<td align="right">0.0%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _SWAP</td>
<td align="right">24,278,270</td>
<td align="right">0.0%</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP _LOAD_FAST_3</td>
<td align="right">24,035,380</td>
<td align="right">0.0%</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE _UNPACK_SEQUENCE_LIST</td>
<td align="right">24,002,040</td>
<td align="right">0.0%</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">23,961,660</td>
<td align="right">0.0%</td>
<td align="right">93.6%</td>
</tr>
</tbody>
</table>


</details>

---

To assess their potency, I've taken the 326 UOp pairs that account for more that 0.1% of all UOp pairs and running them through the scoring script, which compares the length of the superinstruction in machine instructions to the sum of the lengths of its components. Here are those scores, by both percentage difference and absolute difference:

`./python Tools/jit/score.py jit_stencils.h --output_mode "table" --sort_by "delta"`
<details>
<summary>Scoring for top 326 UOp Pairs (x86_64)</summary>

| UOps                                                           | MC Count of Individual Ops | MC Count when Compiled Together | Percentage | Delta |
|----------------------------------------------------------------|:---------------------:|:------------------------------:|:----------:|:-----:|
| _TO_BOOL_INT / _GUARD_IS_TRUE_POP                              | 331                   | 207                            | 62.54%     | -124  |
| _TO_BOOL_NONE / _GUARD_IS_FALSE_POP                            | 243                   | 128                            | 52.67%     | -115  |
| _TO_BOOL_BOOL / _GUARD_IS_FALSE_POP                            | 233                   | 133                            | 57.08%     | -100  |
| _TO_BOOL_BOOL / _GUARD_IS_TRUE_POP                             | 233                   | 133                            | 57.08%     | -100  |
| _GUARD_IS_TRUE_POP / _EXIT_TRACE                               | 201                   | 106                            | 52.74%     | -95   |
| _GUARD_IS_FALSE_POP / _EXIT_TRACE                              | 201                   | 106                            | 52.74%     | -95   |
| _BINARY_OP_MULTIPLY_FLOAT / _BINARY_OP_ADD_FLOAT               | 506                   | 413                            | 81.62%     | -93   |
| _COMPARE_OP_INT / _CHECK_VALIDITY                              | 439                   | 347                            | 79.04%     | -92   |
| _CHECK_MANAGED_OBJECT_HAS_VALUES / _LOAD_ATTR_INSTANCE_VALUE_0 | 325                   | 237                            | 72.92%     | -88   |
| _LIST_APPEND / _JUMP_TO_TOP                                    | 265                   | 184                            | 69.43%     | -81   |
| _JUMP_TO_TOP / _CHECK_VALIDITY                                 | 184                   | 108                            | 58.7%      | -76   |
| _FOR_ITER_TIER_TWO / _CHECK_VALIDITY                           | 360                   | 294                            | 81.67%     | -66   |
| _ITER_CHECK_LIST / _GUARD_NOT_EXHAUSTED_LIST                   | 183                   | 121                            | 66.12%     | -62   |
| _ITER_CHECK_RANGE / _GUARD_NOT_EXHAUSTED_RANGE                 | 171                   | 109                            | 63.74%     | -62   |
| _ITER_CHECK_TUPLE / _GUARD_NOT_EXHAUSTED_TUPLE                 | 183                   | 121                            | 66.12%     | -62   |
| _CHECK_VALIDITY_AND_SET_IP / _CALL_METHOD_DESCRIPTOR_NOARGS    | 622                   | 562                            | 90.35%     | -60   |
| _CHECK_VALIDITY / _ITER_CHECK_LIST                             | 166                   | 108                            | 65.06%     | -58   |
| _CHECK_GLOBALS / _CHECK_BUILTINS                               | 172                   | 114                            | 66.28%     | -58   |
| _CHECK_VALIDITY / _ITER_CHECK_TUPLE                            | 166                   | 108                            | 65.06%     | -58   |
| _RESUME_CHECK / _CHECK_GLOBALS                                 | 169                   | 111                            | 65.68%     | -58   |
| _BINARY_SUBSCR_LIST_INT / _STORE_FAST                          | 388                   | 330                            | 85.05%     | -58   |
| _CHECK_VALIDITY / _CHECK_GLOBALS                               | 162                   | 104                            | 64.2%      | -58   |
| _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT / _GUARD_KEYS_VERSION   | 232                   | 176                            | 75.86%     | -56   |
| _CHECK_VALIDITY / _UNPACK_SEQUENCE_TUPLE                       | 339                   | 283                            | 83.48%     | -56   |
| _CHECK_FUNCTION_EXACT_ARGS / _CHECK_STACK_SPACE                | 313                   | 259                            | 82.75%     | -54   |
| _CHECK_VALIDITY / _RESUME_CHECK                                | 159                   | 105                            | 66.04%     | -54   |
| _CALL_TYPE_1 / _STORE_FAST_5                                   | 422                   | 368                            | 87.2%      | -54   |
| _BINARY_OP_ADD_INT / _STORE_FAST_1                             | 312                   | 260                            | 83.33%     | -52   |
| _CHECK_VALIDITY / _UNPACK_SEQUENCE_TWO_TUPLE                   | 281                   | 229                            | 81.49%     | -52   |
| _BINARY_OP_ADD_INT / _STORE_FAST                               | 327                   | 275                            | 84.1%      | -52   |
| _BINARY_OP_ADD_INT / _STORE_FAST_4                             | 312                   | 260                            | 83.33%     | -52   |
| _CHECK_VALIDITY_AND_SET_IP / _CHECK_FUNCTION_EXACT_ARGS        | 259                   | 208                            | 80.31%     | -51   |
| _BINARY_OP_SUBTRACT_FLOAT / _STORE_FAST                        | 357                   | 307                            | 85.99%     | -50   |
| _BINARY_OP_ADD_FLOAT / _STORE_FAST                             | 357                   | 307                            | 85.99%     | -50   |
| _BINARY_SUBSCR_STR_INT / _STORE_FAST_7                         | 540                   | 491                            | 90.93%     | -49   |
| _CALL_METHOD_DESCRIPTOR_NOARGS / _CHECK_VALIDITY               | 608                   | 562                            | 92.43%     | -46   |
| _STORE_FAST / _STORE_FAST                                      | 208                   | 163                            | 78.37%     | -45   |
| _CALL_BUILTIN_O / _CHECK_VALIDITY                              | 593                   | 548                            | 92.41%     | -45   |
| _STORE_FAST_1 / _STORE_FAST_2                                  | 178                   | 133                            | 74.72%     | -45   |
| _IS_OP / _GUARD_IS_TRUE_POP                                    | 313                   | 268                            | 85.62%     | -45   |
| _STORE_FAST_6 / _STORE_FAST_7                                  | 184                   | 139                            | 75.54%     | -45   |
| _STORE_FAST_7 / _STORE_FAST                                    | 199                   | 154                            | 77.39%     | -45   |
| _STORE_FAST_5 / _STORE_FAST_6                                  | 178                   | 133                            | 74.72%     | -45   |
| _BINARY_SUBSCR_DICT / _CHECK_VALIDITY                          | 409                   | 364                            | 89.0%      | -45   |
| _STORE_SUBSCR_LIST_INT / _CHECK_VALIDITY                       | 377                   | 333                            | 88.33%     | -44   |
| _LOAD_FAST_1 / _BINARY_SUBSCR_STR_INT                          | 477                   | 435                            | 91.19%     | -42   |
| _CALL_ISINSTANCE / _CHECK_VALIDITY                             | 532                   | 490                            | 92.11%     | -42   |
| _CALL_LEN / _CHECK_VALIDITY                                    | 472                   | 430                            | 91.1%      | -42   |
| _COPY / _BINARY_SUBSCR_LIST_INT                                | 338                   | 297                            | 87.87%     | -41   |
| _STORE_SUBSCR_DICT / _CHECK_VALIDITY                           | 338                   | 298                            | 88.17%     | -40   |
| _LOAD_FAST_1 / _UNPACK_SEQUENCE_TUPLE                          | 295                   | 259                            | 87.8%      | -36   |
| _GUARD_BOTH_INT / _BINARY_OP_ADD_INT                           | 348                   | 318                            | 91.38%     | -30   |
| _GUARD_BOTH_INT / _BINARY_OP_SUBTRACT_INT                      | 348                   | 318                            | 91.38%     | -30   |
| _CALL_BUILTIN_FAST / _CHECK_VALIDITY                           | 590                   | 561                            | 95.08%     | -29   |
| _STORE_FAST_1 / _JUMP_TO_TOP                                   | 197                   | 168                            | 85.28%     | -29   |
| _GUARD_BOTH_UNICODE / _COMPARE_OP_STR                          | 335                   | 307                            | 91.64%     | -28   |
| _BINARY_SUBSCR_LIST_INT / _LOAD_CONST_INLINE_BORROW            | 314                   | 286                            | 91.08%     | -28   |
| _BINARY_SUBSCR_LIST_INT / _LOAD_FAST                           | 330                   | 302                            | 91.52%     | -28   |
| _LOAD_CONST_INLINE_BORROW / _BINARY_SUBSCR_LIST_INT            | 314                   | 287                            | 91.4%      | -27   |
| _UNPACK_SEQUENCE_TUPLE / _STORE_FAST_5                         | 352                   | 325                            | 92.33%     | -27   |
| _GUARD_NOT_EXHAUSTED_LIST / _ITER_NEXT_LIST                    | 149                   | 124                            | 83.22%     | -25   |
| _GUARD_NOT_EXHAUSTED_TUPLE / _ITER_NEXT_TUPLE                  | 146                   | 121                            | 82.88%     | -25   |
| _LOAD_CONST_INLINE_BORROW / _STORE_FAST                        | 134                   | 109                            | 81.34%     | -25   |
| _ITER_NEXT_LIST / _STORE_FAST                                  | 160                   | 135                            | 84.38%     | -25   |
| _ITER_NEXT_LIST / _STORE_FAST_5                                | 145                   | 120                            | 82.76%     | -25   |
| _ITER_NEXT_LIST / _STORE_FAST_1                                | 145                   | 120                            | 82.76%     | -25   |
| _ITER_NEXT_TUPLE / _STORE_FAST                                 | 157                   | 132                            | 84.08%     | -25   |
| _ITER_NEXT_TUPLE / _STORE_FAST_4                               | 142                   | 117                            | 82.39%     | -25   |
| _CHECK_VALIDITY / _GUARD_IS_FALSE_POP                          | 194                   | 171                            | 88.14%     | -23   |
| _PUSH_FRAME / _CHECK_VALIDITY                                  | 144                   | 121                            | 84.03%     | -23   |
| _CHECK_VALIDITY / _TO_BOOL_BOOL                                | 191                   | 168                            | 87.96%     | -23   |
| _CHECK_VALIDITY / _GUARD_IS_TRUE_POP                           | 194                   | 171                            | 88.14%     | -23   |
| _CHECK_VALIDITY / _EXIT_TRACE                                  | 159                   | 136                            | 85.53%     | -23   |
| _ITER_NEXT_LIST / _UNPACK_SEQUENCE_TWO_TUPLE                   | 261                   | 238                            | 91.19%     | -23   |
| _CHECK_VALIDITY / _GUARD_BOTH_FLOAT                            | 201                   | 178                            | 88.56%     | -23   |
| _GUARD_IS_TRUE_POP / _JUMP_TO_TOP                              | 226                   | 204                            | 90.27%     | -22   |
| _GUARD_IS_FALSE_POP / _JUMP_TO_TOP                             | 226                   | 204                            | 90.27%     | -22   |
| _LOAD_FAST / _BINARY_OP_MULTIPLY_FLOAT                         | 299                   | 278                            | 92.98%     | -21   |
| _GUARD_TYPE_VERSION / _CHECK_MANAGED_OBJECT_HAS_VALUES         | 253                   | 233                            | 92.09%     | -20   |
| _GUARD_TYPE_VERSION / _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT   | 253                   | 233                            | 92.09%     | -20   |
| _GUARD_BOTH_FLOAT / _BINARY_OP_MULTIPLY_FLOAT                  | 378                   | 358                            | 94.71%     | -20   |
| _STORE_FAST / _LOAD_FAST                                       | 150                   | 130                            | 86.67%     | -20   |
| _GUARD_BOTH_FLOAT / _BINARY_OP_ADD_FLOAT                       | 378                   | 358                            | 94.71%     | -20   |
| _GUARD_BOTH_FLOAT / _BINARY_OP_SUBTRACT_FLOAT                  | 378                   | 358                            | 94.71%     | -20   |
| _STORE_FAST / _LOAD_CONST_INLINE_BORROW                        | 134                   | 114                            | 85.07%     | -20   |
| _STORE_SLICE / _CHECK_VALIDITY                                 | 392                   | 372                            | 94.9%      | -20   |
| _BINARY_OP / _LOAD_FAST_0                                      | 269                   | 249                            | 92.57%     | -20   |
| _BINARY_OP_SUBTRACT_FLOAT / _LOAD_FAST_1                       | 285                   | 265                            | 92.98%     | -20   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_7                             | 153                   | 134                            | 87.58%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_1                             | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_0                             | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_TRUE_POP / _LOAD_FAST_0                              | 150                   | 131                            | 87.33%     | -19   |
| _BINARY_OP_MULTIPLY_FLOAT / _GUARD_BOTH_FLOAT                  | 378                   | 359                            | 94.97%     | -19   |
| _BINARY_SUBSCR_STR_INT / _LOAD_FAST_2                          | 477                   | 458                            | 96.02%     | -19   |
| _GUARD_IS_TRUE_POP / _LOAD_FAST_6                              | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_3                             | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_2                             | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_CONST_INLINE_BORROW                | 148                   | 129                            | 87.16%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST                               | 164                   | 145                            | 88.41%     | -19   |
| _GUARD_IS_FALSE_POP / _LOAD_FAST_5                             | 150                   | 131                            | 87.33%     | -19   |
| _GUARD_IS_TRUE_POP / _LOAD_FAST_1                              | 150                   | 131                            | 87.33%     | -19   |
| _BINARY_OP_ADD_FLOAT / _SWAP                                   | 307                   | 289                            | 94.14%     | -18   |
| _BINARY_OP_ADD_INT / _LOAD_CONST_INLINE_BORROW                 | 253                   | 235                            | 92.89%     | -18   |
| _LOAD_FAST_0 / _GUARD_TYPE_VERSION                             | 153                   | 136                            | 88.89%     | -17   |
| _CHECK_VALIDITY_AND_SET_IP / _LOAD_ATTR                        | 405                   | 388                            | 95.8%      | -17   |
| _COPY / _COPY                                                  | 108                   | 91                             | 84.26%     | -17   |
| _SWAP / _SWAP                                                  | 108                   | 91                             | 84.26%     | -17   |
| _POP_FRAME / _CHECK_VALIDITY                                   | 187                   | 170                            | 90.91%     | -17   |
| _LOAD_FAST / _GUARD_BOTH_FLOAT                                 | 171                   | 154                            | 90.06%     | -17   |
| _LOAD_FAST_2 / _GUARD_BOTH_FLOAT                               | 157                   | 140                            | 89.17%     | -17   |
| _LOAD_FAST_5 / _GUARD_TYPE_VERSION                             | 153                   | 136                            | 88.89%     | -17   |
| _LOAD_FAST_2 / _TO_BOOL_BOOL                                   | 147                   | 130                            | 88.44%     | -17   |
| _LOAD_FAST_1 / _GUARD_TYPE_VERSION                             | 153                   | 136                            | 88.89%     | -17   |
| _LOAD_FAST_3 / _GUARD_TYPE_VERSION                             | 153                   | 136                            | 88.89%     | -17   |
| _COPY / _TO_BOOL_BOOL                                          | 169                   | 152                            | 89.94%     | -17   |
| _LOAD_CONST_INLINE_BORROW / _COPY                              | 84                    | 67                             | 79.76%     | -17   |
| _POP_FRAME / _CHECK_VALIDITY_AND_SET_IP                        | 201                   | 184                            | 91.54%     | -17   |
| _LOAD_FAST / _COPY                                             | 100                   | 83                             | 83.0%      | -17   |
| _LOAD_FAST_7 / _LOAD_CONST_INLINE_BORROW                       | 65                    | 49                             | 75.38%     | -16   |
| _LOAD_FAST_0 / _LOAD_FAST_1                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_FAST_1 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _LOAD_FAST_5 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _LOAD_FAST_7 / _LOAD_FAST_3                                    | 67                    | 51                             | 76.12%     | -16   |
| _LOAD_FAST / _LOAD_CONST_INLINE_BORROW                         | 76                    | 60                             | 78.95%     | -16   |
| _LOAD_CONST_INLINE_WITH_NULL / _LOAD_FAST_5                    | 78                    | 62                             | 79.49%     | -16   |
| _GUARD_KEYS_VERSION / _LOAD_ATTR_METHOD_WITH_VALUES            | 149                   | 133                            | 89.26%     | -16   |
| _LOAD_CONST_INLINE_BORROW / _LOAD_CONST_INLINE_BORROW          | 60                    | 44                             | 73.33%     | -16   |
| _LOAD_FAST / _LOAD_FAST                                        | 92                    | 76                             | 82.61%     | -16   |
| _GUARD_TYPE_VERSION / _LOAD_ATTR_METHOD_NO_DICT                | 170                   | 154                            | 90.59%     | -16   |
| _GUARD_TYPE_VERSION / _LOAD_ATTR_SLOT_0                        | 309                   | 293                            | 94.82%     | -16   |
| _LOAD_FAST_6 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _GUARD_IS_FALSE_POP / _LOAD_CONST_INLINE_WITH_NULL             | 164                   | 148                            | 90.24%     | -16   |
| _LOAD_FAST_3 / _LOAD_FAST_4                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_CONST_INLINE_WITH_NULL / _LOAD_FAST_1                    | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_FAST_2 / _LOAD_FAST_3                                    | 64                    | 48                             | 75.0%      | -16   |
| _CHECK_STACK_SPACE / _INIT_CALL_PY_EXACT_ARGS_4                | 637                   | 621                            | 97.49%     | -16   |
| _LOAD_FAST_1 / _LOAD_FAST                                      | 78                    | 62                             | 79.49%     | -16   |
| _CHECK_STACK_SPACE / _INIT_CALL_PY_EXACT_ARGS_1                | 594                   | 578                            | 97.31%     | -16   |
| _LOAD_FAST_4 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _UNPACK_SEQUENCE_TWO_TUPLE / _STORE_FAST_1                     | 294                   | 278                            | 94.56%     | -16   |
| _LOAD_FAST / _LOAD_FAST_2                                      | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_CONST_INLINE_BORROW / _LOAD_FAST                         | 76                    | 60                             | 78.95%     | -16   |
| _LOAD_FAST_1 / _LOAD_FAST_2                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_FAST_6 / _LOAD_FAST                                      | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_CONST_INLINE_BORROW_WITH_NULL / _LOAD_FAST_1             | 70                    | 54                             | 77.14%     | -16   |
| _LOAD_FAST_5 / _LOAD_CONST_INLINE                              | 70                    | 54                             | 77.14%     | -16   |
| _PUSH_NULL / _LOAD_FAST_0                                      | 56                    | 40                             | 71.43%     | -16   |
| _LOAD_FAST / _TO_BOOL_INT                                      | 259                   | 243                            | 93.82%     | -16   |
| _LOAD_FAST_1 / _LOAD_FAST_4                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_FAST_4 / _LOAD_FAST                                      | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_FAST / _PUSH_NULL                                        | 70                    | 54                             | 77.14%     | -16   |
| _LOAD_CONST_INLINE_WITH_NULL / _LOAD_FAST_0                    | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_FAST_2 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _LOAD_FAST_0 / _LOAD_FAST                                      | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_CONST_INLINE_WITH_NULL / _LOAD_FAST_2                    | 78                    | 62                             | 79.49%     | -16   |
| _LOAD_CONST_INLINE_BORROW / _LOAD_FAST_2                       | 62                    | 46                             | 74.19%     | -16   |
| _LOAD_FAST_3 / _LOAD_CONST_INLINE_BORROW                       | 62                    | 46                             | 74.19%     | -16   |
| _LOAD_FAST_7 / _LOAD_FAST                                      | 81                    | 65                             | 80.25%     | -16   |
| _LOAD_FAST_2 / _LOAD_FAST_7                                    | 67                    | 51                             | 76.12%     | -16   |
| _LOAD_FAST_7 / _LOAD_FAST_2                                    | 67                    | 51                             | 76.12%     | -16   |
| _LOAD_FAST_3 / _LOAD_FAST_5                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_CONST_INLINE_WITH_NULL / _LOAD_FAST_3                    | 78                    | 62                             | 79.49%     | -16   |
| _CHECK_STACK_SPACE / _INIT_CALL_PY_EXACT_ARGS_2                | 603                   | 587                            | 97.35%     | -16   |
| _LOAD_FAST_2 / _LOAD_FAST_5                                    | 64                    | 48                             | 75.0%      | -16   |
| _PUSH_NULL / _LOAD_FAST_2                                      | 56                    | 40                             | 71.43%     | -16   |
| _LOAD_FAST_4 / _LOAD_FAST_0                                    | 64                    | 48                             | 75.0%      | -16   |
| _LOAD_FAST_2 / _PUSH_NULL                                      | 56                    | 40                             | 71.43%     | -16   |
| _LOAD_FAST_1 / _LOAD_FAST_0                                    | 64                    | 48                             | 75.0%      | -16   |
| _GUARD_BOTH_INT / _COMPARE_OP_INT                              | 488                   | 473                            | 96.93%     | -15   |
| _CHECK_VALIDITY_AND_SET_IP / _LOAD_GLOBAL                      | 458                   | 443                            | 96.72%     | -15   |
| _LOAD_CONST_INLINE_BORROW / _SET_IP                            | 57                    | 44                             | 77.19%     | -13   |
| _SET_IP / _GUARD_BOTH_INT                                      | 152                   | 139                            | 91.45%     | -13   |
| _SET_IP / _GUARD_TYPE_VERSION                                  | 148                   | 135                            | 91.22%     | -13   |
| _SET_IP / _CONTAINS_OP                                         | 287                   | 274                            | 95.47%     | -13   |
| _LOAD_FAST_1 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_0                                 | 108                   | 95                             | 87.96%     | -13   |
| _LOAD_FAST_3 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_1                                 | 108                   | 95                             | 87.96%     | -13   |
| _LOAD_FAST_0 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _SAVE_RETURN_OFFSET / _PUSH_FRAME                              | 95                    | 82                             | 86.32%     | -13   |
| _CHECK_VALIDITY / _SET_IP                                      | 103                   | 90                             | 87.38%     | -13   |
| _SET_IP / _GUARD_BOTH_UNICODE                                  | 152                   | 139                            | 91.45%     | -13   |
| _SET_IP / _COMPARE_OP_STR                                      | 237                   | 224                            | 94.51%     | -13   |
| _SET_IP / _BINARY_SUBSCR                                       | 250                   | 237                            | 94.8%      | -13   |
| _LOAD_FAST / _SET_IP                                           | 73                    | 60                             | 82.19%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST                                   | 122                   | 109                            | 89.34%     | -13   |
| _LOAD_FAST_2 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _LOAD_FAST_4 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _SET_IP / _CHECK_FUNCTION_EXACT_ARGS                           | 196                   | 183                            | 93.37%     | -13   |
| _CHECK_VALIDITY / _LOAD_CONST_INLINE_BORROW                    | 106                   | 93                             | 87.74%     | -13   |
| _SET_IP / _ITER_CHECK_RANGE                                    | 117                   | 104                            | 88.89%     | -13   |
| _SET_IP / _LOAD_ATTR                                           | 342                   | 329                            | 96.2%      | -13   |
| _LOAD_ATTR_METHOD_WITH_VALUES / _CHECK_VALIDITY                | 125                   | 112                            | 89.6%      | -13   |
| _SET_IP / _BINARY_OP                                           | 264                   | 251                            | 95.08%     | -13   |
| _RESUME_CHECK / _LOAD_FAST_0                                   | 115                   | 102                            | 88.7%      | -13   |
| _BINARY_OP_ADD_INT / _SET_IP                                   | 250                   | 237                            | 94.8%      | -13   |
| _SET_IP / _BINARY_OP_ADD_INT                                   | 250                   | 237                            | 94.8%      | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_2                                 | 108                   | 95                             | 87.96%     | -13   |
| _CHECK_BUILTINS / _LOAD_CONST_INLINE_WITH_NULL                 | 132                   | 119                            | 90.15%     | -13   |
| _LOAD_ATTR_INSTANCE_VALUE_0 / _SET_IP                          | 220                   | 207                            | 94.09%     | -13   |
| _LOAD_CONST_INLINE / _SET_IP                                   | 65                    | 52                             | 80.0%      | -13   |
| _SWAP / _SET_IP                                                | 81                    | 68                             | 83.95%     | -13   |
| _SET_IP / _LOAD_DEREF                                          | 181                   | 168                            | 92.82%     | -13   |
| _LOAD_ATTR_SLOT_0 / _SET_IP                                    | 215                   | 202                            | 93.95%     | -13   |
| _INIT_CALL_PY_EXACT_ARGS_4 / _SAVE_RETURN_OFFSET               | 520                   | 507                            | 97.5%      | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_6                                 | 108                   | 95                             | 87.96%     | -13   |
| _SET_IP / _STORE_SUBSCR_LIST_INT                               | 328                   | 315                            | 96.04%     | -13   |
| _LOAD_ATTR_METHOD_NO_DICT / _CHECK_VALIDITY_AND_SET_IP         | 139                   | 126                            | 90.65%     | -13   |
| _SET_IP / _BUILD_TUPLE                                         | 207                   | 194                            | 93.72%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_5                                 | 108                   | 95                             | 87.96%     | -13   |
| _INIT_CALL_PY_EXACT_ARGS_1 / _SAVE_RETURN_OFFSET               | 477                   | 464                            | 97.27%     | -13   |
| _CHECK_STACK_SPACE / _INIT_CALL_PY_EXACT_ARGS_0                | 596                   | 583                            | 97.82%     | -13   |
| _INIT_CALL_PY_EXACT_ARGS_0 / _SAVE_RETURN_OFFSET               | 479                   | 466                            | 97.29%     | -13   |
| _LOAD_ATTR_METHOD_NO_DICT / _CHECK_VALIDITY                    | 125                   | 112                            | 89.6%      | -13   |
| _SET_IP / _FOR_ITER_TIER_TWO                                   | 311                   | 298                            | 95.82%     | -13   |
| _SET_IP / _STORE_SUBSCR                                        | 297                   | 284                            | 95.62%     | -13   |
| _CHECK_BUILTINS / _LOAD_CONST_INLINE_BORROW_WITH_NULL          | 124                   | 111                            | 89.52%     | -13   |
| _CHECK_BUILTINS / _LOAD_CONST_INLINE_BORROW                    | 116                   | 103                            | 88.79%     | -13   |
| _SET_IP / _POP_FRAME                                           | 138                   | 125                            | 90.58%     | -13   |
| _STORE_FAST_2 / _SET_IP                                        | 116                   | 103                            | 88.79%     | -13   |
| _LOAD_FAST_5 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _LOAD_ATTR_INSTANCE_VALUE_0 / _LOAD_FAST_1                     | 225                   | 212                            | 94.22%     | -13   |
| _CHECK_GLOBALS / _LOAD_CONST_INLINE_WITH_NULL                  | 132                   | 119                            | 90.15%     | -13   |
| _SET_IP / _BUILD_LIST                                          | 207                   | 194                            | 93.72%     | -13   |
| _LOAD_FAST_7 / _SET_IP                                         | 62                    | 49                             | 79.03%     | -13   |
| _GUARD_IS_FALSE_POP / _CHECK_GLOBALS                           | 204                   | 191                            | 93.63%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_3                                 | 108                   | 95                             | 87.96%     | -13   |
| _COPY / _SET_IP                                                | 81                    | 68                             | 83.95%     | -13   |
| _LOAD_CONST_INLINE_BORROW / _EXIT_TRACE                        | 113                   | 100                            | 88.5%      | -13   |
| _CHECK_GLOBALS / _LOAD_CONST_INLINE                            | 124                   | 111                            | 89.52%     | -13   |
| _CHECK_VALIDITY / _LOAD_FAST_4                                 | 108                   | 95                             | 87.96%     | -13   |
| _BINARY_OP_SUBTRACT_INT / _SET_IP                              | 250                   | 237                            | 94.8%      | -13   |
| _GUARD_IS_TRUE_POP / _CHECK_GLOBALS                            | 204                   | 191                            | 93.63%     | -13   |
| _SET_IP / _BINARY_SUBSCR_DICT                                  | 360                   | 347                            | 96.39%     | -13   |
| _SET_IP / _STORE_SLICE                                         | 343                   | 330                            | 96.21%     | -13   |
| _SET_IP / _BINARY_OP_MULTIPLY_INT                              | 250                   | 237                            | 94.8%      | -13   |
| _SET_IP / _BUILD_SLICE                                         | 381                   | 368                            | 96.59%     | -13   |
| _LOAD_FAST_3 / _CHECK_GLOBALS                                  | 118                   | 105                            | 88.98%     | -13   |
| _BINARY_OP / _SET_IP                                           | 264                   | 251                            | 95.08%     | -13   |
| _CHECK_VALIDITY / _PUSH_NULL                                   | 100                   | 87                             | 87.0%      | -13   |
| _SET_IP / _GET_ITER                                            | 192                   | 179                            | 93.23%     | -13   |
| _SET_IP / _LIST_EXTEND                                         | 355                   | 342                            | 96.34%     | -13   |
| _SET_IP / _GET_ANEXT                                           | 390                   | 377                            | 96.67%     | -13   |
| _SET_IP / _TO_BOOL                                             | 210                   | 197                            | 93.81%     | -13   |
| _LOAD_ATTR_METHOD_WITH_VALUES / _CHECK_VALIDITY_AND_SET_IP     | 139                   | 126                            | 90.65%     | -13   |
| _SET_IP / _STORE_SUBSCR_DICT                                   | 289                   | 276                            | 95.5%      | -13   |
| _SET_IP / _BINARY_OP_SUBTRACT_INT                              | 250                   | 237                            | 94.8%      | -13   |
| _STORE_FAST_1 / _SET_IP                                        | 116                   | 103                            | 88.79%     | -13   |
| _LOAD_FAST_6 / _SET_IP                                         | 59                    | 46                             | 77.97%     | -13   |
| _LOAD_ATTR_INSTANCE_VALUE_0 / _LOAD_FAST_0                     | 225                   | 212                            | 94.22%     | -13   |
| _SET_IP / _BINARY_SLICE                                        | 278                   | 265                            | 95.32%     | -13   |
| _STORE_FAST / _SET_IP                                          | 131                   | 118                            | 90.08%     | -13   |
| _LOAD_FAST_5 / _CHECK_GLOBALS                                  | 118                   | 105                            | 88.98%     | -13   |
| _LOAD_FAST_1 / _EXIT_TRACE                                     | 115                   | 102                            | 88.7%      | -13   |
| _RESUME_CHECK / _LOAD_FAST_1                                   | 115                   | 102                            | 88.7%      | -13   |
| _INIT_CALL_PY_EXACT_ARGS_2 / _SAVE_RETURN_OFFSET               | 486                   | 473                            | 97.33%     | -13   |
| _LOAD_ATTR / _CHECK_VALIDITY                                   | 391                   | 379                            | 96.93%     | -12   |
| _BUILD_TUPLE / _CHECK_VALIDITY                                 | 256                   | 244                            | 95.31%     | -12   |
| _BINARY_OP_MULTIPLY_FLOAT / _EXIT_TRACE                        | 336                   | 324                            | 96.43%     | -12   |
| _BUILD_LIST / _CHECK_VALIDITY                                  | 256                   | 244                            | 95.31%     | -12   |
| _GUARD_TYPE_VERSION / _GUARD_DORV_VALUES                       | 201                   | 189                            | 94.03%     | -12   |
| _BUILD_TUPLE / _CHECK_VALIDITY_AND_SET_IP                      | 270                   | 258                            | 95.56%     | -12   |
| _CONTAINS_OP / _CHECK_VALIDITY                                 | 336                   | 325                            | 96.73%     | -11   |
| _BINARY_SUBSCR / _CHECK_VALIDITY                               | 299                   | 288                            | 96.32%     | -11   |
| _SET_IP / _CALL_BUILTIN_FAST                                   | 541                   | 530                            | 97.97%     | -11   |
| _SET_IP / _CALL_BUILTIN_O                                      | 544                   | 533                            | 97.98%     | -11   |
| _CHECK_VALIDITY_AND_SET_IP / _BINARY_SUBSCR                    | 313                   | 302                            | 96.49%     | -11   |
| _CHECK_VALIDITY_AND_SET_IP / _BINARY_OP                        | 327                   | 316                            | 96.64%     | -11   |
| _LOAD_ATTR_INSTANCE_VALUE_0 / _GUARD_BOTH_FLOAT                | 318                   | 307                            | 96.54%     | -11   |
| _CHECK_VALIDITY / _STORE_FAST_0                                | 165                   | 154                            | 93.33%     | -11   |
| _LOAD_FAST_3 / _TO_BOOL_NONE                                   | 157                   | 146                            | 92.99%     | -11   |
| _COMPARE_OP / _CHECK_VALIDITY                                  | 412                   | 401                            | 97.33%     | -11   |
| _CHECK_VALIDITY_AND_SET_IP / _POP_FRAME                        | 201                   | 191                            | 95.02%     | -10   |
| _CHECK_VALIDITY / _STORE_FAST                                  | 180                   | 171                            | 95.0%      | -9    |
| _ITER_NEXT_RANGE / _CHECK_VALIDITY                             | 204                   | 195                            | 95.59%     | -9    |
| _LOAD_DEREF / _CHECK_VALIDITY                                  | 230                   | 221                            | 96.09%     | -9    |
| _CHECK_VALIDITY / _STORE_FAST_6                                | 165                   | 156                            | 94.55%     | -9    |
| _CHECK_VALIDITY / _STORE_FAST_3                                | 165                   | 156                            | 94.55%     | -9    |
| _CHECK_VALIDITY / _POP_TOP                                     | 152                   | 143                            | 94.08%     | -9    |
| _SET_IP / _CALL_ISINSTANCE                                     | 483                   | 474                            | 98.14%     | -9    |
| _LOAD_FAST_1 / _CALL_TYPE_1                                    | 365                   | 356                            | 97.53%     | -9    |
| _SET_IP / _CALL_LEN                                            | 423                   | 414                            | 97.87%     | -9    |
| _CHECK_VALIDITY / _STORE_FAST_4                                | 165                   | 156                            | 94.55%     | -9    |
| _CHECK_VALIDITY / _STORE_FAST_7                                | 171                   | 162                            | 94.74%     | -9    |
| _BINARY_SUBSCR_LIST_INT / _SET_IP                              | 311                   | 302                            | 97.11%     | -9    |
| _CHECK_VALIDITY_AND_SET_IP / _CALL_INTRINSIC_1                 | 276                   | 267                            | 96.74%     | -9    |
| _CALL_INTRINSIC_1 / _CHECK_VALIDITY                            | 262                   | 253                            | 96.56%     | -9    |
| _GET_ITER / _CHECK_VALIDITY                                    | 241                   | 232                            | 96.27%     | -9    |
| _CHECK_VALIDITY / _STORE_FAST_1                                | 165                   | 156                            | 94.55%     | -9    |
| _GUARD_NOT_EXHAUSTED_RANGE / _ITER_NEXT_RANGE                  | 209                   | 201                            | 96.17%     | -8    |
| _STORE_FAST / _LOAD_FAST_0                                     | 136                   | 128                            | 94.12%     | -8    |
| _STORE_FAST / _LOAD_FAST_1                                     | 136                   | 128                            | 94.12%     | -8    |
| _LOAD_ATTR / _CHECK_VALIDITY_AND_SET_IP                        | 405                   | 397                            | 98.02%     | -8    |
| _STORE_FAST_1 / _LOAD_FAST_0                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_3 / _LOAD_FAST_3                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST / _LOAD_FAST_6                                     | 136                   | 128                            | 94.12%     | -8    |
| _STORE_FAST_5 / _LOAD_FAST_5                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_4 / _LOAD_FAST_4                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_5 / _LOAD_FAST_3                                   | 121                   | 113                            | 93.39%     | -8    |
| _POP_TOP / _LOAD_FAST_0                                        | 108                   | 100                            | 92.59%     | -8    |
| _STORE_FAST / _LOAD_FAST_4                                     | 136                   | 128                            | 94.12%     | -8    |
| _STORE_FAST_0 / _LOAD_FAST_0                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_4 / _LOAD_FAST_1                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_7 / _LOAD_FAST_3                                   | 127                   | 119                            | 93.7%      | -8    |
| _STORE_FAST_2 / _LOAD_FAST_2                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_1 / _LOAD_FAST_1                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_3 / _LOAD_FAST_2                                   | 121                   | 113                            | 93.39%     | -8    |
| _STORE_FAST_5 / _LOAD_FAST_4                                   | 121                   | 113                            | 93.39%     | -8    |
| _GET_ANEXT / _CHECK_VALIDITY                                   | 439                   | 432                            | 98.41%     | -7    |
| _GUARD_DORV_VALUES / _STORE_ATTR_INSTANCE_VALUE                | 264                   | 257                            | 97.35%     | -7    |
| _COMPARE_OP_STR / _CHECK_VALIDITY                              | 286                   | 280                            | 97.9%      | -6    |
| _STORE_FAST_7 / _LOAD_FAST_7                                   | 130                   | 125                            | 96.15%     | -5    |
| _STORE_FAST / _LOAD_FAST_7                                     | 139                   | 134                            | 96.4%      | -5    |
| _STORE_SUBSCR / _CHECK_VALIDITY                                | 346                   | 342                            | 98.84%     | -4    |
| _CHECK_VALIDITY / _JUMP_TO_TOP                                 | 184                   | 180                            | 97.83%     | -4    |
| _LOAD_GLOBAL / _CHECK_VALIDITY                                 | 444                   | 443                            | 99.77%     | -1    |
| _STORE_FAST_6 / _LOAD_CONST_INLINE_WITH_NULL                   | 135                   | 136                            | 100.74%    | 1     |
| _CHECK_VALIDITY / _IS_OP                                       | 271                   | 273                            | 100.74%    | 2     |
| _TO_BOOL / _CHECK_VALIDITY                                     | 259                   | 262                            | 101.16%    | 3     |
| _BUILD_SLICE / _CHECK_VALIDITY_AND_SET_IP                      | 444                   | 453                            | 102.03%    | 9     |
| _LIST_EXTEND / _CHECK_VALIDITY_AND_SET_IP                      | 418                   | 435                            | 104.07%    | 17    |
| _START_EXECUTOR / _CHECK_VALIDITY                              | 162                   | 180                            | 111.11%    | 18    |
| _START_EXECUTOR / _CHECK_VALIDITY_AND_SET_IP                   | 176                   | 194                            | 110.23%    | 18    |
| _LOAD_ATTR_INSTANCE_VALUE_0 / _TO_BOOL_BOOL                    | 308                   | 326                            | 105.84%    | 18    |
| _LOAD_ATTR_SLOT_0 / _TO_BOOL_BOOL                              | 303                   | 321                            | 105.94%    | 18    |
| _STORE_ATTR_INSTANCE_VALUE / _CHECK_VALIDITY                   | 260                   | 279                            | 107.31%    | 19    |

</details>

---

So, how much shorter is "short enough to be worth it?" Should we be weighting the instructions also by their prevalence? Probably some experimentation is needed.

I tried a couple arbitrary testing points - two local runs using pyperformance and one Brandt kindly ran on the benchrunner system. All are compared against main-with-jit.

---

<details>
<summary>Using the 83 pairs* that reduce the machine code count by 20 or more: ~2% Faster (Local)</summary>

Benchmarks with tag 'apps':
===========================

| Benchmark      | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------|:--------:|:----------------------------------:|
| 2to3           | 297 ms   | 292 ms: 1.02x faster               |
| chameleon      | 6.51 ms  | 6.38 ms: 1.02x faster              |
| docutils       | 2.74 sec | 2.65 sec: 1.03x faster             |
| Geometric mean | (ref)    | 1.01x faster                       |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------------------------|:--------:|:----------------------------------:|
| async_tree_eager_tg              | 83.6 ms  | 77.0 ms: 1.09x faster              |
| async_tree_io                    | 1.12 sec | 1.06 sec: 1.05x faster             |
| async_tree_memoization_tg        | 551 ms   | 530 ms: 1.04x faster               |
| async_tree_eager_memoization     | 275 ms   | 264 ms: 1.04x faster               |
| async_tree_io_tg                 | 1.11 sec | 1.08 sec: 1.03x faster             |
| async_tree_eager_memoization_tg  | 206 ms   | 201 ms: 1.02x faster               |
| async_tree_none_tg               | 423 ms   | 415 ms: 1.02x faster               |
| async_tree_memoization           | 541 ms   | 533 ms: 1.02x faster               |
| async_tree_cpu_io_mixed_tg       | 733 ms   | 741 ms: 1.01x slower               |
| async_tree_eager_cpu_io_mixed    | 473 ms   | 478 ms: 1.01x slower               |
| async_tree_eager_io              | 1.06 sec | 1.09 sec: 1.02x slower             |
| async_tree_eager_cpu_io_mixed_tg | 409 ms   | 420 ms: 1.03x slower               |
| Geometric mean                   | (ref)    | 1.01x faster                       |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_eager, async_tree_none, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------|:--------:|:----------------------------------:|
| nbody          | 85.3 ms  | 78.9 ms: 1.08x faster              |
| float          | 78.1 ms  | 76.6 ms: 1.02x faster              |
| Geometric mean | (ref)    | 1.03x faster                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------|:--------:|:----------------------------------:|
| regex_compile  | 172 ms   | 169 ms: 1.02x faster               |
| regex_effbot   | 2.74 ms  | 2.75 ms: 1.01x slower              |
| regex_dna      | 160 ms   | 161 ms: 1.01x slower               |
| regex_v8       | 21.4 ms  | 21.9 ms: 1.02x slower              |
| Geometric mean | (ref)    | 1.00x slower                       |

Benchmarks with tag 'serialize':
================================

| Benchmark          | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|--------------------|:--------:|:----------------------------------:|
| tomli_loads        | 2.24 sec | 2.13 sec: 1.05x faster             |
| pickle_dict        | 32.3 us  | 31.5 us: 1.03x faster              |
| pickle_pure_python | 291 us   | 286 us: 1.02x faster               |
| xml_etree_process  | 63.4 ms  | 62.5 ms: 1.01x faster              |
| json_loads         | 27.0 us  | 26.7 us: 1.01x faster              |
| json_dumps         | 10.6 ms  | 10.5 ms: 1.01x faster              |
| pickle             | 11.7 us  | 11.6 us: 1.01x faster              |
| pickle_list        | 4.96 us  | 4.93 us: 1.01x faster              |
| Geometric mean     | (ref)    | 1.01x faster                       |

Benchmark hidden because not significant (6): unpickle, xml_etree_iterparse, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|------------------------|:--------:|:----------------------------------:|
| python_startup_no_site | 12.4 ms  | 12.8 ms: 1.03x slower              |
| Geometric mean         | (ref)    | 1.01x slower                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------|:--------:|:----------------------------------:|
| mako           | 11.4 ms  | 11.0 ms: 1.04x faster              |
| genshi_text    | 24.9 ms  | 24.2 ms: 1.03x faster              |
| genshi_xml     | 62.6 ms  | 63.3 ms: 1.01x slower              |
| Geometric mean | (ref)    | 1.02x faster                       |

All benchmarks:
===============

| Benchmark                        | main-jit | uop-stats-20-mc-or-better-pairs-83 |
|----------------------------------|:--------:|:----------------------------------:|
| unpack_sequence                  | 136 ns   | 97.7 ns: 1.39x faster              |
| bench_mp_pool                    | 42.0 ms  | 32.9 ms: 1.28x faster              |
| pathlib                          | 21.8 ms  | 19.1 ms: 1.15x faster              |
| async_tree_eager_tg              | 83.6 ms  | 77.0 ms: 1.09x faster              |
| deepcopy                         | 378 us   | 349 us: 1.08x faster               |
| nbody                            | 85.3 ms  | 78.9 ms: 1.08x faster              |
| deltablue                        | 3.77 ms  | 3.52 ms: 1.07x faster              |
| hexiom                           | 8.28 ms  | 7.76 ms: 1.07x faster              |
| scimark_monte_carlo              | 73.2 ms  | 69.4 ms: 1.05x faster              |
| async_tree_io                    | 1.12 sec | 1.06 sec: 1.05x faster             |
| tomli_loads                      | 2.24 sec | 2.13 sec: 1.05x faster             |
| raytrace                         | 307 ms   | 292 ms: 1.05x faster               |
| dask                             | 687 ms   | 654 ms: 1.05x faster               |
| deepcopy_reduce                  | 3.31 us  | 3.17 us: 1.04x faster              |
| telco                            | 8.19 ms  | 7.88 ms: 1.04x faster              |
| async_tree_memoization_tg        | 551 ms   | 530 ms: 1.04x faster               |
| async_tree_eager_memoization     | 275 ms   | 264 ms: 1.04x faster               |
| mako                             | 11.4 ms  | 11.0 ms: 1.04x faster              |
| pyflate                          | 507 ms   | 489 ms: 1.04x faster               |
| spectral_norm                    | 115 ms   | 111 ms: 1.04x faster               |
| docutils                         | 2.74 sec | 2.65 sec: 1.03x faster             |
| richards_super                   | 56.0 ms  | 54.2 ms: 1.03x faster              |
| deepcopy_memo                    | 37.0 us  | 35.9 us: 1.03x faster              |
| genshi_text                      | 24.9 ms  | 24.2 ms: 1.03x faster              |
| meteor_contest                   | 101 ms   | 98.3 ms: 1.03x faster              |
| scimark_fft                      | 331 ms   | 322 ms: 1.03x faster               |
| pickle_dict                      | 32.3 us  | 31.5 us: 1.03x faster              |
| logging_simple                   | 6.95 us  | 6.77 us: 1.03x faster              |
| crypto_pyaes                     | 76.2 ms  | 74.2 ms: 1.03x faster              |
| async_tree_io_tg                 | 1.11 sec | 1.08 sec: 1.03x faster             |
| asyncio_tcp                      | 394 ms   | 385 ms: 1.02x faster               |
| async_tree_eager_memoization_tg  | 206 ms   | 201 ms: 1.02x faster               |
| scimark_lu                       | 145 ms   | 142 ms: 1.02x faster               |
| coverage                         | 370 ms   | 361 ms: 1.02x faster               |
| logging_format                   | 8.01 us  | 7.84 us: 1.02x faster              |
| sqlglot_optimize                 | 60.2 ms  | 58.9 ms: 1.02x faster              |
| chameleon                        | 6.51 ms  | 6.38 ms: 1.02x faster              |
| generators                       | 26.7 ms  | 26.2 ms: 1.02x faster              |
| float                            | 78.1 ms  | 76.6 ms: 1.02x faster              |
| async_tree_none_tg               | 423 ms   | 415 ms: 1.02x faster               |
| sqlglot_transpile                | 1.63 ms  | 1.60 ms: 1.02x faster              |
| regex_compile                    | 172 ms   | 169 ms: 1.02x faster               |
| sqlite_synth                     | 2.56 us  | 2.52 us: 1.02x faster              |
| 2to3                             | 297 ms   | 292 ms: 1.02x faster               |
| pickle_pure_python               | 291 us   | 286 us: 1.02x faster               |
| sqlglot_normalize                | 115 ms   | 113 ms: 1.02x faster               |
| typing_runtime_protocols         | 122 us   | 120 us: 1.02x faster               |
| async_tree_memoization           | 541 ms   | 533 ms: 1.02x faster               |
| go                               | 151 ms   | 149 ms: 1.01x faster               |
| xml_etree_process                | 63.4 ms  | 62.5 ms: 1.01x faster              |
| richards                         | 49.3 ms  | 48.7 ms: 1.01x faster              |
| dulwich_log                      | 83.9 ms  | 83.0 ms: 1.01x faster              |
| sqlglot_parse                    | 1.31 ms  | 1.29 ms: 1.01x faster              |
| json_loads                       | 27.0 us  | 26.7 us: 1.01x faster              |
| json_dumps                       | 10.6 ms  | 10.5 ms: 1.01x faster              |
| pickle                           | 11.7 us  | 11.6 us: 1.01x faster              |
| pickle_list                      | 4.96 us  | 4.93 us: 1.01x faster              |
| comprehensions                   | 18.2 us  | 18.1 us: 1.01x faster              |
| asyncio_tcp_ssl                  | 1.33 sec | 1.32 sec: 1.00x faster             |
| regex_effbot                     | 2.74 ms  | 2.75 ms: 1.01x slower              |
| regex_dna                        | 160 ms   | 161 ms: 1.01x slower               |
| coroutines                       | 22.2 ms  | 22.3 ms: 1.01x slower              |
| async_generators                 | 419 ms   | 423 ms: 1.01x slower               |
| async_tree_cpu_io_mixed_tg       | 733 ms   | 741 ms: 1.01x slower               |
| asyncio_websockets               | 442 ms   | 447 ms: 1.01x slower               |
| async_tree_eager_cpu_io_mixed    | 473 ms   | 478 ms: 1.01x slower               |
| genshi_xml                       | 62.6 ms  | 63.3 ms: 1.01x slower              |
| scimark_sor                      | 140 ms   | 142 ms: 1.01x slower               |
| create_gc_cycles                 | 1.06 ms  | 1.08 ms: 1.02x slower              |
| async_tree_eager_io              | 1.06 sec | 1.09 sec: 1.02x slower             |
| regex_v8                         | 21.4 ms  | 21.9 ms: 1.02x slower              |
| async_tree_eager_cpu_io_mixed_tg | 409 ms   | 420 ms: 1.03x slower               |
| python_startup_no_site           | 12.4 ms  | 12.8 ms: 1.03x slower              |
| Geometric mean                   | (ref)    | 1.02x faster                       |

Benchmark hidden because not significant (24): pprint_safe_repr, fannkuch, nqueens, unpickle, gc_traversal, xml_etree_iterparse, python_startup, scimark_sparse_mat_mult, tornado_http, chaos, unpickle_list, unpickle_pure_python, async_tree_cpu_io_mixed, logging_silent, pprint_pformat, async_tree_eager, xml_etree_generate, pidigits, async_tree_none, html5lib, mdp, async_tree_eager_io_tg, xml_etree_parse, bench_thread_pool

</details>

<details>
<summary>Using the 251 pairs* that reduce the machine code count by 13 or more: ~4% Faster (Local)</summary>

Benchmarks with tag 'apps':
===========================

| Benchmark      | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------|:--------:|:-----------------------------------:|
| 2to3           | 297 ms   | 284 ms: 1.04x faster                |
| docutils       | 2.74 sec | 2.62 sec: 1.05x faster              |
| Geometric mean | (ref)    | 1.02x faster                        |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------------------------|:--------:|:-----------------------------------:|
| async_tree_eager_tg              | 83.6 ms  | 77.5 ms: 1.08x faster               |
| async_tree_memoization_tg        | 551 ms   | 522 ms: 1.05x faster                |
| async_tree_io_tg                 | 1.11 sec | 1.06 sec: 1.05x faster              |
| async_tree_io                    | 1.12 sec | 1.07 sec: 1.05x faster              |
| async_tree_memoization           | 541 ms   | 518 ms: 1.04x faster                |
| async_tree_eager_cpu_io_mixed_tg | 409 ms   | 392 ms: 1.04x faster                |
| async_tree_eager_cpu_io_mixed    | 473 ms   | 455 ms: 1.04x faster                |
| async_tree_eager_memoization     | 275 ms   | 265 ms: 1.04x faster                |
| async_tree_cpu_io_mixed          | 732 ms   | 708 ms: 1.03x faster                |
| async_tree_cpu_io_mixed_tg       | 733 ms   | 718 ms: 1.02x faster                |
| async_tree_eager_memoization_tg  | 206 ms   | 202 ms: 1.02x faster                |
| async_tree_eager                 | 116 ms   | 114 ms: 1.02x faster                |
| Geometric mean                   | (ref)    | 1.03x faster                        |

Benchmark hidden because not significant (4): async_tree_none, async_tree_eager_io, async_tree_none_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------|:--------:|:-----------------------------------:|
| nbody          | 85.3 ms  | 77.2 ms: 1.11x faster               |
| float          | 78.1 ms  | 74.9 ms: 1.04x faster               |
| pidigits       | 191 ms   | 183 ms: 1.04x faster                |
| Geometric mean | (ref)    | 1.06x faster                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------|:--------:|:-----------------------------------:|
| regex_compile  | 172 ms   | 162 ms: 1.06x faster                |
| regex_dna      | 160 ms   | 161 ms: 1.00x slower                |
| regex_v8       | 21.4 ms  | 21.8 ms: 1.02x slower               |
| Geometric mean | (ref)    | 1.01x faster                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------------|:--------:|:-----------------------------------:|
| tomli_loads          | 2.24 sec | 2.06 sec: 1.09x faster              |
| pickle_dict          | 32.3 us  | 31.5 us: 1.03x faster               |
| unpickle_pure_python | 244 us   | 238 us: 1.03x faster                |
| xml_etree_parse      | 142 ms   | 140 ms: 1.01x faster                |
| pickle_list          | 4.96 us  | 4.89 us: 1.01x faster               |
| pickle_pure_python   | 291 us   | 287 us: 1.01x faster                |
| xml_etree_iterparse  | 103 ms   | 102 ms: 1.01x faster                |
| pickle               | 11.7 us  | 11.5 us: 1.01x faster               |
| xml_etree_process    | 63.4 ms  | 62.9 ms: 1.01x faster               |
| json_dumps           | 10.6 ms  | 10.5 ms: 1.01x faster               |
| xml_etree_generate   | 94.0 ms  | 93.5 ms: 1.01x faster               |
| unpickle             | 15.6 us  | 15.8 us: 1.01x slower               |
| Geometric mean       | (ref)    | 1.02x faster                        |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|------------------------|:--------:|:-----------------------------------:|
| python_startup         | 13.4 ms  | 13.6 ms: 1.02x slower               |
| python_startup_no_site | 12.4 ms  | 12.7 ms: 1.02x slower               |
| Geometric mean         | (ref)    | 1.02x slower                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------|:--------:|:-----------------------------------:|
| mako           | 11.4 ms  | 10.8 ms: 1.05x faster               |
| genshi_text    | 24.9 ms  | 23.9 ms: 1.04x faster               |
| genshi_xml     | 62.6 ms  | 61.3 ms: 1.02x faster               |
| Geometric mean | (ref)    | 1.04x faster                        |

All benchmarks:
===============

| Benchmark                        | main-jit | uop-stats-13-mc-or-better-pairs-251 |
|----------------------------------|:--------:|:-----------------------------------:|
| unpack_sequence                  | 136 ns   | 98.7 ns: 1.38x faster               |
| pathlib                          | 21.8 ms  | 18.9 ms: 1.16x faster               |
| scimark_monte_carlo              | 73.2 ms  | 65.0 ms: 1.13x faster               |
| pyflate                          | 507 ms   | 450 ms: 1.13x faster                |
| hexiom                           | 8.28 ms  | 7.43 ms: 1.11x faster               |
| nbody                            | 85.3 ms  | 77.2 ms: 1.11x faster               |
| deltablue                        | 3.77 ms  | 3.44 ms: 1.10x faster               |
| raytrace                         | 307 ms   | 281 ms: 1.09x faster                |
| tomli_loads                      | 2.24 sec | 2.06 sec: 1.09x faster              |
| pprint_safe_repr                 | 946 ms   | 870 ms: 1.09x faster                |
| pprint_pformat                   | 1.99 sec | 1.83 sec: 1.08x faster              |
| deepcopy                         | 378 us   | 349 us: 1.08x faster                |
| async_tree_eager_tg              | 83.6 ms  | 77.5 ms: 1.08x faster               |
| spectral_norm                    | 115 ms   | 107 ms: 1.07x faster                |
| scimark_fft                      | 331 ms   | 311 ms: 1.07x faster                |
| crypto_pyaes                     | 76.2 ms  | 71.5 ms: 1.07x faster               |
| regex_compile                    | 172 ms   | 162 ms: 1.06x faster                |
| dask                             | 687 ms   | 646 ms: 1.06x faster                |
| chaos                            | 69.1 ms  | 65.1 ms: 1.06x faster               |
| richards_super                   | 56.0 ms  | 52.8 ms: 1.06x faster               |
| richards                         | 49.3 ms  | 46.5 ms: 1.06x faster               |
| async_tree_memoization_tg        | 551 ms   | 522 ms: 1.05x faster                |
| mako                             | 11.4 ms  | 10.8 ms: 1.05x faster               |
| telco                            | 8.19 ms  | 7.79 ms: 1.05x faster               |
| deepcopy_reduce                  | 3.31 us  | 3.15 us: 1.05x faster               |
| deepcopy_memo                    | 37.0 us  | 35.2 us: 1.05x faster               |
| async_tree_io_tg                 | 1.11 sec | 1.06 sec: 1.05x faster              |
| async_tree_io                    | 1.12 sec | 1.07 sec: 1.05x faster              |
| docutils                         | 2.74 sec | 2.62 sec: 1.05x faster              |
| async_tree_memoization           | 541 ms   | 518 ms: 1.04x faster                |
| coverage                         | 370 ms   | 354 ms: 1.04x faster                |
| 2to3                             | 297 ms   | 284 ms: 1.04x faster                |
| nqueens                          | 97.4 ms  | 93.4 ms: 1.04x faster               |
| async_tree_eager_cpu_io_mixed_tg | 409 ms   | 392 ms: 1.04x faster                |
| genshi_text                      | 24.9 ms  | 23.9 ms: 1.04x faster               |
| float                            | 78.1 ms  | 74.9 ms: 1.04x faster               |
| logging_simple                   | 6.95 us  | 6.68 us: 1.04x faster               |
| pidigits                         | 191 ms   | 183 ms: 1.04x faster                |
| sqlglot_optimize                 | 60.2 ms  | 57.9 ms: 1.04x faster               |
| sqlglot_transpile                | 1.63 ms  | 1.57 ms: 1.04x faster               |
| async_tree_eager_cpu_io_mixed    | 473 ms   | 455 ms: 1.04x faster                |
| logging_format                   | 8.01 us  | 7.72 us: 1.04x faster               |
| fannkuch                         | 423 ms   | 408 ms: 1.04x faster                |
| async_tree_eager_memoization     | 275 ms   | 265 ms: 1.04x faster                |
| comprehensions                   | 18.2 us  | 17.6 us: 1.04x faster               |
| scimark_sparse_mat_mult          | 4.82 ms  | 4.66 ms: 1.03x faster               |
| async_tree_cpu_io_mixed          | 732 ms   | 708 ms: 1.03x faster                |
| go                               | 151 ms   | 147 ms: 1.03x faster                |
| meteor_contest                   | 101 ms   | 98.4 ms: 1.03x faster               |
| sqlglot_parse                    | 1.31 ms  | 1.27 ms: 1.03x faster               |
| pickle_dict                      | 32.3 us  | 31.5 us: 1.03x faster               |
| unpickle_pure_python             | 244 us   | 238 us: 1.03x faster                |
| sqlite_synth                     | 2.56 us  | 2.49 us: 1.03x faster               |
| gc_traversal                     | 3.31 ms  | 3.22 ms: 1.03x faster               |
| scimark_lu                       | 145 ms   | 142 ms: 1.02x faster                |
| dulwich_log                      | 83.9 ms  | 82.1 ms: 1.02x faster               |
| async_tree_cpu_io_mixed_tg       | 733 ms   | 718 ms: 1.02x faster                |
| sqlglot_normalize                | 115 ms   | 112 ms: 1.02x faster                |
| genshi_xml                       | 62.6 ms  | 61.3 ms: 1.02x faster               |
| async_tree_eager_memoization_tg  | 206 ms   | 202 ms: 1.02x faster                |
| create_gc_cycles                 | 1.06 ms  | 1.05 ms: 1.02x faster               |
| async_tree_eager                 | 116 ms   | 114 ms: 1.02x faster                |
| xml_etree_parse                  | 142 ms   | 140 ms: 1.01x faster                |
| pickle_list                      | 4.96 us  | 4.89 us: 1.01x faster               |
| asyncio_tcp_ssl                  | 1.33 sec | 1.31 sec: 1.01x faster              |
| pickle_pure_python               | 291 us   | 287 us: 1.01x faster                |
| xml_etree_iterparse              | 103 ms   | 102 ms: 1.01x faster                |
| pickle                           | 11.7 us  | 11.5 us: 1.01x faster               |
| generators                       | 26.7 ms  | 26.5 ms: 1.01x faster               |
| xml_etree_process                | 63.4 ms  | 62.9 ms: 1.01x faster               |
| json_dumps                       | 10.6 ms  | 10.5 ms: 1.01x faster               |
| xml_etree_generate               | 94.0 ms  | 93.5 ms: 1.01x faster               |
| asyncio_websockets               | 442 ms   | 441 ms: 1.00x faster                |
| regex_dna                        | 160 ms   | 161 ms: 1.00x slower                |
| async_generators                 | 419 ms   | 421 ms: 1.01x slower                |
| unpickle                         | 15.6 us  | 15.8 us: 1.01x slower               |
| coroutines                       | 22.2 ms  | 22.4 ms: 1.01x slower               |
| python_startup                   | 13.4 ms  | 13.6 ms: 1.02x slower               |
| regex_v8                         | 21.4 ms  | 21.8 ms: 1.02x slower               |
| logging_silent                   | 103 ns   | 105 ns: 1.02x slower                |
| python_startup_no_site           | 12.4 ms  | 12.7 ms: 1.02x slower               |
| Geometric mean                   | (ref)    | 1.04x faster                        |

Benchmark hidden because not significant (16): bench_mp_pool, async_tree_none, tornado_http, typing_runtime_protocols, chameleon, unpickle_list, json_loads, asyncio_tcp, scimark_sor, regex_effbot, async_tree_eager_io, async_tree_none_tg, mdp, html5lib, async_tree_eager_io_tg, bench_thread_pool

</details>

[Using the 251 pairs* that reduce the machine code count by 13 or more: ~4% Faster (Benchrunner)]()

---

*\*Not including pairs that include `_JUMP_TO_TOP` - currently, including that in a superinstruction currently segfaults.*