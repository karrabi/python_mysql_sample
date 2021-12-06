import Database as db


def main():
    DB = db.DB('tempdb002')
    # DB.InsertRecord(field01='test02', field02=125)

    # result = DB.GetAllRecords()
    # for row in result:
    #     print(row)

    result = DB.GetRecord(row_id=3)
    for row in result:
        print(row[0])
        print(row[1])
        print(row[2])


if __name__ == '__main__':
    main()