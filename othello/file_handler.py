

class FileHandler:
    """Class that holds functionality to handle scores file of othello"""

    @staticmethod
    def open_and_read(file):
        """
        Parameters
        -------------------
        file (string): file name

        Returns
        ----------------
        list

        Opens and reads text file as comma separated list.
        """
        f = open(file)
        text_file_as_list = f.readlines()
        return text_file_as_list

    @staticmethod
    def compare_all_values(txtf_list, new_score):
        """
        Parameters
        ----------------------
        txtf_list (list): a list of strings
        new_score (string): user name and score

        Returns
        -----------------------
        list

        Compares new score to all scores of list. If new_score
        is largest val then it is appened to the beginning of list.
        If not, appened to the end.
        """
        try:
            sorted_list = sorted(txtf_list,
                                 key=lambda x: int(x.strip().split()[-1]),
                                 reverse=True)
            my_new_score = int(new_score.strip().split()[-1])
            top_score = int(sorted_list[0].strip().split()[-1])
            if my_new_score >= top_score:
                txtf_list.insert(0, new_score)
            else:
                txtf_list.append(new_score)
            return txtf_list
        except IndexError:  # In the case scores.txt is empty
            pass

    @staticmethod
    def overwrite_txtfile(txt_file, txtf_list, new_score):
        """
        Parameters
        ------------------
        txt_file (string): text file
        txtf_list (list): a list of strings
        new_score (string): user name and score

        Returns
        --------------------------
        None

        Overwrites text file with new list.
        """
        f = open(txt_file, "w")
        try:
            for score in txtf_list:
                f.write(score)
        except TypeError:
            f.write(new_score)
        f.close()
