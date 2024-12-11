class test {
    public void method1() {
        print("Method 1");
        randomChance(0.5) {
            print("works1");
        }
        6-diceRoll(3) {
            print("works2");
        }
        coinFlip() {
            heads {
                print("works3");
            }
            tails {
                print("works4");
            }
        }
        repeatUntilSuccess(randomChance(0.9)) {
            print("Works5");
        }
    }  

    public void method2() {
        print("Method 2");
        slotMachine();
        let x = randomRange(0,100);
        print(x);
    }

    public void method3() {
        print("Method 3");
        for (int i = 1; i < 10; i = i + 1) [chance(0.25)] {
            if (i % 5 == 0) {
                print("Fizz");
            }
            else if (i % 3 == 0) {
                print("Buzz");
            }
            else {
                print(i);
            }
        }
        for (int i = 1; i < 10; i = i + 1) [chance(0.25)] {
            print(i);
        }
    }
}