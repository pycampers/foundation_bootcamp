"""
        <tr>
            <th>Name</th>
            <th>Telephone</th>
        </tr>
        <tr>
            <td>Bill Gates</td>
            <td>55577854</td>
        </tr>
"""

def make_html_table_from_dict(data_dict):
    row_template = "<tr>{}</tr>"


    header_row = ''
    for key in data_dict[0].keys():
        row = f'<th>{key}</th>\n'
        header_row += row


    data_rows = ''
    for single_data_dict in data_dict:
        value_row = ''
        for value in single_data_dict.values():
            row = f'<td>{value}</td>\n'
            value_row += row

        data_rows += row_template.format(value_row)

    final_html_table = row_template.format(header_row) + data_rows
    return final_html_table

data_dict = [{"Name": "Bill Gates", "Telephone": "12345678"},
             {"Name": "Steve Jobs", "Telephone": "98765432"}]

# print(make_html_table_from_dict(data_dict))
