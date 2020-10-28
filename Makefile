# Author: Ashley Yeung
#
# This is the Makefile for our Sprout Social Preternship Project

PP := g++

FLAGS := -O0 -g -Wall
CXXFLAGS := -m64 -std=c++11 $(FLAGS)
PQCFLAGS := -O0 -g -Wall -Wextra -Wconversion -Wshadow -pedantic -Werror -lm
PQCXX := -m64 -stdc++11 -Weffc++ $(PQCFLAGS)

INC := include
SRC := src
OBJ := obj
EXE := exe

# Command: make main
mainObjs := $(OBJ)/main.o $(OBJ)Universal.o

main: $(mainObjs)
	$(PP) $(CXXFLAGS) -o $(EXE)/main $(mainObjs)
	$(EXE)/./mainObjs

$(OBJ)/main.o: $(SRC)/main.cpp $(INC)/Universal.h
	$(PP) $(CXXFLAGS) -c $(SRC)/main.cpp -o $@

$(OBJ)/Universal.o: $(INC)/Universal.cpp $(INC)/Universal.h
	$(PP) $(CXXFLAGS) -c $(INC)/Universal.cpp -o $@

# Command: make initialize
initialize:
	mkdir $(OBJ) $(EXE)

# Command: make all
all: main

# Command: make clean
clean:
	rm -rf *.o $(OBJ)/* $(EXE)/*
