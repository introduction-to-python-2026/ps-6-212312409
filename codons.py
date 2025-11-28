def create_codon_dict(file_path):
    f = open(file_path,"r")
    rows = f.readlines()
    f.close()

    dict = {}
    for row in rows:
      cell = row.strip().split('\t')
      key = cell[0]
      value = cell[2]
      dict[key] = value

    return dict
    




