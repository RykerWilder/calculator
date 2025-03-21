from math import sqrt;

menu_message = """
    1. Per effettuare un'addizione.
    2. Per effettuare una sottrazione.
    3. Per effettuare una moltiplicazione.
    4. Per effettuare una divisione.
    5. Per effettuare una radice quadrata.
    6. Per uscire dal programma.
""";

while True:
    print(menu_message);
    action = input("Seleziona un'operazione da effettuare: ");

    if action == "1":
        factors = int(input("Di quanti fattori ha bisogno la tua somma?: "));
        factorList = [];
        result = 0;

        for factor in range(factors):
            item = int(input(f"Inserisci il {factor + 1} numero "));
            factorList.append(item);

        for number in factorList:
            result += number;
        print("Il risultato dell'addizione è: ", result);

    elif action == "2":
        factors = int(input("Di quanti fattori ha bisogno la tua sottrazione?: "));
        factorList = [];
        result = 0;

        for factor in range(factors):
            item = int(input(f"Inserisci il {factor + 1} numero "));
            factorList.append(item);

        for number in factorList:
            result -= number;
        print("Il risultato della sottrazione è: ", result);

    elif action == "3":
        a = float(input("Inserisci il primo fattore: "));
        b = float(input("Inserisci il secondo fattore: "));
        print("Il risultato della moltiplicazione è: ", str(a * b));
    elif action == "4":
        a = float(input("Inserisci il dividendo: "));
        b = float(input("Inserisci il divisore: "));
        print("Il risultato della divisione è: ", str(a / b));
    elif action == "5":
        a = float(input("Inserisci il radicando: "));
        print("Il risultato della radice quadrata è: ", str(sqrt(a)));
    elif action == '6':
        print("Hai selezionato 'uscire dal programma', a presto!");
        break;