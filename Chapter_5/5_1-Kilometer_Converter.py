MILES_MULTIPLER= 0.6214

def get_kilometers():
    km = 0.0
    return float(input('Введите количество километров: '))

def km_to_miles_converter(kilometers):
    m = 0.0
    return kilometers * MILES_MULTIPLER

def main():    
    km = get_kilometers()
    miles = km_to_miles_converter(km)
    print(f'{km:,.2f} километров будет {miles:,.2f} миль.')

main()
