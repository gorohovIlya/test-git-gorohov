.DEFAULT_GOAL := help

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating demo-practice"
	mkdir -p ${PRACTICE}
remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Removing demo-practice"
	rm -rf ${PRACTICE}
help:
	@echo "This Makefile for repo-level activity"

# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md
