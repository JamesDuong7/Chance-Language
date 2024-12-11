from os.path import dirname, join
from textx import metamodel_from_file
import random

class JavaInterpreter:
    def readLines(self, model):
        for c in model.members:
            if c.__class__.__name__ == "MethodDeclaration":
                # create dictionary in this scope
                dict = {}
                for statement in c.statements:
                    dict = self.interpret(statement, dict)
    
    # interpret each statement in method
    def interpret(self, line, dict):
        method_name = f"interpret_{line.__class__.__name__}"
        method = getattr(self, method_name)
        return method(line, dict)
    
    '''
    print(x);
    '''
    def interpret_PrintStatement(self, line, dict):
        try:
            try:
                print(eval(line.output, {}, dict))
            except TypeError and SyntaxError:
                print(line.output)
        except NameError:
            print(line.output)
        return dict
    
    def interpret_VariableDeclaration(self, line, dict):
        try:
            dict[line.name] = eval(line.value, {}, dict)
        except TypeError:
            dict[line.name] = line.value
        return dict


    '''
    if (i % 5 == 0) {
    }
    else if (i % 3 == 0) {
    }
    else {
    }
    '''
    def interpret_IfStatement(self, line, dict):
        if eval(line.condition, {}, dict):
            for stmt in line.trueBranch:
                self.interpret(stmt, dict)
        else:
            self.interpret_ElseIfStatement(line, dict)

    def interpret_ElseIfStatement(self, line, dict):
        for elif_block in line.elseifBranches:
            if eval(elif_block.condition, {}, dict):
                for stmt in elif_block.body:
                    self.interpret(stmt, dict)
                return
        for stmt in line.falseBranch:
            self.interpret(stmt, dict)
    

    '''
    while (x < 100) [chance(0.25)] {
    }
    '''
    def interpret_WhileLoop(self, line, dict):
        while eval(line.condition, {}, dict):
            for stmt in line.body:
                self.interpret(stmt, dict)
            # loop breaks depending on probability
            if random.random() <= line.probability:
                break
        return dict

    '''
    for (int i = 0; i < 100; i = i + 1) [chance(0.25)] {
    }
    '''
    def interpret_ForLoop(self, line, dict):
        self.interpret(line.initialization, dict)
        while eval(line.condition, {}, dict):
            for stmt in line.body:
                self.interpret(stmt, dict)
            self.interpret(line.update, dict)
            # loop breaks depending on probability
            if random.random() <= line.probability:
                break
        return dict

    '''
    coinFlip() {
        heads {
        }
        tails {
        }
    }
    '''
    def interpret_CoinFlip(self, line, dict):
        flip_result = random.choice(["heads", "tails"])
        if flip_result == "heads":
            for stmt in line.headsBody:
                self.interpret(stmt, dict)
        else:
            for stmt in line.tailsBody:
                self.interpret(stmt, dict)
        return dict

    '''
    randomChance(0.25) {
    }
    '''
    def interpret_RandomChance(self, line, dict):
        if random.random() <= line.chance:
            for stmt in line.body:
                self.interpret(stmt, dict)
        return dict

    '''
    6-diceRoll(3) {
    }
    '''
    def interpret_DiceRoll(self, line, dict):
        roll = random.randint(1, line.dice) 
        if roll <= line.pick: 
            for stmt in line.body: 
                self.interpret(stmt, dict)

    '''
    let x = randomRange(0, 100);
    '''
    def interpret_RandomRangeExpression(self, line, dict):
        dict[line.name] = random.randint(line.start, line.end)
        return dict
    
    '''
    repeatUntilSuccess(randomChance(0.25)) {
    }
    '''
    def interpret_RepeatUntilSuccess(self, line, dict):
        while (not random.random() <= line.probability):
            for stmt in line.body:
                self.interpret(stmt, dict)
        return dict
            
    '''
    slotMachine();
    '''
    def interpret_SlotMachineExpression(self, line, dict):
        print("Spinning the slot machine...")

        slots = [random.choice(["🍒", "🍋", "🍉", "⭐", "💎", "🔔", "🍇"]) for _ in range(3)]
        print(f"Results: {' '.join(slots)}")

        if len(set(slots)) == 1:
            print("JACKPOT! All three match!")
        elif len(set(slots)) == 2:
            print("You win! Two symbols match!")
        else: 
            print("No matches. Better luck next time!")
        return dict

def main(debug=False):
    this_folder = dirname(__file__)

    # read grammar file, 'grammar.tx'
    program_mm = metamodel_from_file(join(this_folder, 'grammar.tx'), debug=False)

    # interpret file, 'program.cl'
    program_model = program_mm.model_from_file(join(this_folder, 'program.cl'))

    interpreter = JavaInterpreter()
    interpreter.readLines(program_model)

if __name__ == "__main__":
    main()
