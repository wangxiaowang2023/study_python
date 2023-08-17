# -*- coding: utf-8 -*-
def get_full_name(first_name:str,last_name:str)->str:
    new_name=first_name.title()+''+last_name.title()
    return new_name


if __name__ == '__main__':
    get_full_name()