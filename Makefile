.DEFAULT_GOAL := help

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating demo-practice"
	mkdir -p ${PRACTICE}
	cp PracticeMakefile $(PRACTICE)/Makefile
remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Removing demo-practice"
	rm -rf ${PRACTICE}
help:
	@echo "This Makefile for repo-level activity"
