def test(_pdf_dir, _fileName):
    from pdfrw import PdfReader, PdfWriter
    _pdf_file = _pdf_dir + _fileName + ".pdf"
    pdf_rdr = PdfReader(_pdf_file)
    print('hi')
    pdf_rdr.Info.Keywords = "키워드"
    pdf_rdr.Info.Subject = "주제"
    PdfWriter(_pdf_file, trailer=pdf_rdr).write()
    print(pdf_rdr.Info.Keywords)
    print(pdf_rdr.Info)


if __name__ == "__main__":
    import os

    test(os.getcwd() + '/pdf/', 'abcdef')
    print('hi')
