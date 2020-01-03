from email_modules.email_reader import (main as email_reader_main)
# import email_sender from email/email_sender

# import excel_create from excel/excel_create

# import calc_manager from calculators/calc_manager

from translators.translator_manager import (main as translator_manager_main)
# import spearhead_translator from translators/spearhead_translator
# import table_translator from translators/table_translator

if __name__ == "__main__":
    email_list = email_reader_main()
    parameter_list = translator_manager_main(email_list)