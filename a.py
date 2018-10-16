#!/usr/bin/env python3

trs = 4
tbs = 5

to_ignore = (
	(4, 9),
	(4, 5),
)
for r_s, b_s in to_ignore:
	if trs == r_s and tbs == b_s:
		break
else:
	raise UserWarning(f'not sure how to handle')

