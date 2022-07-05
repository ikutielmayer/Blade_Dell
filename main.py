import os

TEST_HOST = 'localhost'
TEST_USERNAME = 'root'
TEST_PASSWORD = 'P@ssw0rd'
myversion = ''

def main():
        myversion = str(os.system(f"racadm -r {TEST_HOST} -u {TEST_USERNAME} -p {TEST_PASSWORD} swinventory --nocertwarn"))
        print(myversion)


if __name__ == '__main__':
    main()
