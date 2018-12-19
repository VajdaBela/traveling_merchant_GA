class Evoluitivni:
    """interface za sve klase koji zele da koriste GA"""
    def mutiraj(self):
        """koristi se za mutiranje jedinku
        input:
            self
        output:
            self"""
        raise NotImplementedError(self.__class__ + ": mutiraj nije implementiran")

    def ukrsti(self, partner):
        """koristi se za ukrstanje jedinki
        input:
            self
            partner-istog tipa kao self,jedan u paru koji cini potomke
        output:
            deca-dvoclana lista koja sadrzi dva potomka"""
        raise NotImplementedError(self.__class__ + ": ukrsti nije implementiran")

    def getFtines(self):
        """koristi se za procenu dobrote jedinke
        input:
            self
        output:
            fitnes-realni broj, obelezava nivo savrsenstva"""
        raise NotImplementedError(self.__class__ + ": getFitness nije implementiran")