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
        a = float(input("Inserisci il primo numero: "));
        b = float(input("Inserisci il secondo numero: "));
        print("Il risultato dell'addizione è: ", str(a + b));
    elif action == "2":
        a = float(input("Inserisci il minuendo: "));
        b = float(input("Inserisci il sottraendo: "));
        print("Il risultato della sottrazione è: ", str(a - b));
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