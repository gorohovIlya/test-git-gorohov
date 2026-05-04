.PHONY: another-app

# Might be correct, but `build` and `app` are different names
build:
	gcc main.c -o app

# correct no PHONY
app: main.c
	gcc main.c -o app

# incorrect: listed in PHONY
another-app: main.c
	gcc main.c -o another-app
