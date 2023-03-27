import platform

def main():
    if platform.system() == 'Darwin':
        from . import mac
    else:
        from . import windows

if __name__ == "__main__":
    main()
