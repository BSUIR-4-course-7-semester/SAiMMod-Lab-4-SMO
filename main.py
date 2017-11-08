from Mediator import Mediator


def main():
    p = float(input('p:'))
    p1 = float(input('p1:'))
    p2 = float(input('p2:'))
    c = int(input('c:'))
    mediator = Mediator(p, p1, p2, c)
    mediator.run()

if __name__ == "__main__":
    main()