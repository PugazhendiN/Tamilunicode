class Tamilscript:
    """Collection of Tamil characters"""
    def eluthuvagai(self):
        """This method returns the classifications of Tamil letter """
        return [x[i]['vagai'] for i in range(len(x))]
    def uyir_eluthu(self):
        """This method returns the Uyir eluthukkal in Tamil language"""
        return(x[0]['vadivam'])
    def mey_eluthu(self):
        """This method returns the mey eluthukkal in Tamil language"""
        return(x[1]['vadivam'])
    def uyir_mei_eluthu(self):
        """This method returns the Uyir mey eluthukkal in Tamil language"""
        for i in range(len(x[2]['vadivam'])):
            for j in x[2]['vadivam'][i].keys(): 
                print(f'{j}')
                for k in x[2]['vadivam'][i].values():
                    print(k)
    def aayutha_eluthu(self):
        """This method returns the aayutha eluthu in Tamil language"""
        return(x[3]['vadivam'])
    def vada_eluthu(self):
        """This method returns the vada eluthukkal in Tamil language"""
        for i in range(len(x[4]['vadivam'])):
            for j in x[4]['vadivam'][i].keys(): 
                print(f'{j}')
                for k in x[4]['vadivam'][i].values():
                    print(k)
