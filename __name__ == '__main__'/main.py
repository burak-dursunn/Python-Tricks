from my_module import func


def main():
    func()


if __name__ == '__main__':
    main()
# Bu şekilde kodumuz daha güvenli ve okunaklı oldu.
# Eğer bu dosya bir modül olarak başka bir dosya tarafından import edilirse, main fonksiyonu çalışmayacak.
