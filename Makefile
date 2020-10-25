PP := g++

FLAGS := -O0 -g -Wall
CXXFLAGS := -m64 -std=c++11 $(FLAGS)
PQC := -O0 -g -Wall -Wextra -Wconversion -Wshadow -pedantic -Werror -lm
PQCXX := -m64 -std=c++11 -Weffc++ $(PQCFLAGS)

INC := include
SRC := src
OBJ := obj
EXE := exe

# Command make Universal
UniversalObjs := $(OBJ)/main.o $(OBJ)/Universal.o

$(OBJ)/main.o $(SRC)/main.cpp $(INC)/Universal.h
  $(PP) $(CXXFLAGS) -c $(SRC)/main.cpp

$(OBJ)/Universal.o $(SRC)/main.cpp $(INC)/Universal.h
  $(PP) $(CXXFLAGS) -c $(SRC)/Universal.cpp
