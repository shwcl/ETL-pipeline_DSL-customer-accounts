

import csv


input_file = open('C:\\jobs\\DSL_accounts_to_terminated\\in\\name_address_data.csv')

csv_reader_obj = csv.reader(input_file)

g_name_data = []
g_address_data = []

output_file = open('C:\\jobs\\DSL_accounts_to_terminated\\out\\name_address_output.csv', 'w')
output_file.write('gpon_number' + ',' + 'account_number' + ','
                  + 'g_name_substring_found_in_dsl_name' + ',' + 'g_address_substring_found_in_dsl_address' + ','
                  + 'g_name_substring_found_in_ll_name' + ',' + 'g_address_substring_found_in_ll_address' + ','
				  + 'g_name_array_length' + ',' + 'g_address_array_length' + ',' 
				  + 'dsl_name_array_length' + ',' + 'dsl_address_array_length' + ','
				  + 'll_name_array_length' + ',' + 'll_address_array_length' + '\n')

output_file.close()

g_name_substring_found_in_dsl_name = 0
g_name_substring_found_in_ll_name = 0
g_address_substring_found_in_dsl_address = 0
g_address_substring_found_in_ll_address = 0

for row in csv_reader_obj:
    if csv_reader_obj.line_num != 1:

        g_name_data = row[2].split(" ")
        for item in g_name_data:
            if len(item) > 0 and item in (row[4].split(" ")):
                g_name_substring_found_in_dsl_name += 1

            if len(item) > 0 and item in (row[6].split(" ")):
                g_name_substring_found_in_ll_name += 1

        g_address_data = row[3].split(" ")
        for item in g_address_data:
            if len(item) > 0 and item in (row[5].split(" ")):
                g_address_substring_found_in_dsl_address += 1

            if len(item) > 0 and item in (row[7].split(" ")):
                g_address_substring_found_in_ll_address += 1


        output_file = open('C:\\jobs\\DSL_accounts_to_terminated\\out\\name_address_output.csv', 'a')
        output_file.write(row[0] + ',' + row[1] + ','  
                          + str(g_name_substring_found_in_dsl_name) + ',' + str(g_address_substring_found_in_dsl_address) + ','
                          + str(g_name_substring_found_in_ll_name) + ',' + str(g_address_substring_found_in_ll_address) + ','
						   + row[8] + ',' + row[9] + ',' + row[10] + ',' + row[11]  + ',' + row[12] + ',' + row[13] + '\n')

        output_file.close()
        g_name_substring_found_in_dsl_name = 0
        g_name_substring_found_in_ll_name = 0
        g_address_substring_found_in_dsl_address = 0
        g_address_substring_found_in_ll_address = 0

input_file.close()