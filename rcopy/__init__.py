import platform

def main():
    if platform.system() == 'Darwin':
        import mac
    else:
        import windows

if __name__ == "__main__":
    main()
