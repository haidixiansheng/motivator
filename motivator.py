import random

ans = ["5 minutes late", \
"ru coming to the backend meeting?", \
"I feel nervous if ...", \
"Can you write a doc?", \
"so people can comment", \
"List the pros and cons for each approach", \
"Let's do a fast iteration ", \
"Can you work on them in parallel?", \
"What's the ETA", \
"What is the short term goal, mid-term goal?", \
"Can you do it in [half of the proposed ETA]", \
"Talk to ", \
"Fang ", \
"Neha ", \
"Emma ", \
"When I was working on", \
"Opening Hour", \
"Chain", \
"Id forwarding", \
"Is it possible you just ping him/her", \
"This should be very simple", \
"I want to XYZ as soon as possible", \
"What is the status on XYZ?"\
]


while True:
	t = raw_input()
	print(ans[random.randrange(len(ans))])
