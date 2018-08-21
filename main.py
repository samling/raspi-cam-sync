import pigpio

pi1 = pigpio.pi('192.168.88.149')
pi2 = pigpio.pi('192.168.88.55')
INPUT_PIN = 11

def main():
    if pi1.read(INPUT_PIN) == 0:
        pi1.write(INPUT_PIN, 1)
        print("pi1 GPIO pin %s set to 1" % INPUT_PIN)
        print(pi1.read(INPUT_PIN))
    else:
        pi1.write(INPUT_PIN, 0)
        print("pi1 GPIO pin %s set to 0" % INPUT_PIN)
        print(pi1.read(INPUT_PIN))

    if pi2.read(INPUT_PIN) == 0:
        pi2.write(INPUT_PIN, 1)
        print("pi2 GPIO pin %s set to 1" % INPUT_PIN)
        print(pi2.read(INPUT_PIN))
    else:
        pi2.write(INPUT_PIN, 0)
        print("pi2 GPIO pin %s set to 0" % INPUT_PIN)
        print(pi2.read(INPUT_PIN))

if __name__ == '__main__':
    main()
