from characters import Monster, Player


def play():
    skeleton = Monster('Skeleton', 50, 10, 0)
    player = Player()

    skeleton.attack(player)
    player.attack(skeleton)
    player.attack(skeleton)
    player.attack(skeleton)
    player.attack(skeleton)


def main():
    print("""
     ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗
     ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║
     ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║
     ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║
     ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
    """)

    print("<S>TART GAME")
    print("<L>OAD GAME")
    print("<Q>UIT GAME")

    while True:
        k = input()
        if k.upper() == 'S':
            play()
        elif k.upper() == 'L':
            print('Loading game...')
        if k.lower() == 'q':
            break


if __name__ == '__main__':
    main()
