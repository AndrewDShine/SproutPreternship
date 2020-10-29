PP := g++

FLAGS := -O0 -g -Wall
CXXFLAGS := -m64 -std=c++11 $(FLAGS)
PQC := -O0 -g -Wall -Wextra -Wconversion -Wshadow -pedantic -Werror -lm
PQCXX := -m64 -std=c++11 -Weffc++ $(PQCFLAGS)

INC := include
SRC := src
OBJ := obj
EXE := exe

# Command: make Universal
UniversalObjs := $(OBJ)/main.o $(OBJ)/Universal.o

Universal: $(UniversalObjs)
	$(PP) $(CXXFLAGS) -o $(EXE)/Universal $(UniversalObjs)
	$(EXE)/./Universal

$(OBJ)/main.o: $(SRC)/main.cpp $(INC)/Universal.h
	$(PP) $(CXXFLAGS) -c $(SRC)/main.cpp -o $@

$(OBJ)/Universal.o: $(SRC)/Universal.cpp $(INC)/Universal.h
	$(PP) $(CXXFLAGS) -c $(SRC)/Universal.cpp -o $@

# Command: make initialize
initialize:
	mkdir  $(OBJ) $(EXE)

clean:
	rm -rf *.o $(OBJ)/* $(EXE)/*
