new_text = 'Vete a la mierda'
def write_to_csv(new_text):
    import csv
    with open('test.csv', "w") as test_file:
        test_writer = csv.writer(test_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='')
        test_writer.writerow(['','text'])
        test_writer.writerow(['0', new_text])
    
write_to_csv(new_text)

