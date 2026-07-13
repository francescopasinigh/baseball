import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.dd1 = None
        self._node = None





    def fillDDYear(self, dd: ft.Dropdown()):
        years = self._model._allYears

        if dd is self._view._ddAnno:
            for f in years:
                dd.options.append(ft.dropdown.Option(text=f.year,
                                                     data=f.year,
                                                     on_click=self.read_DD_Rating1))

    def read_DD_Rating1(self, e):

        if e.control.data is None:
            self.dd1 = None
            self.loadNodes(self._view._ddSquadra)
            self._view.update_page()

        else:
            print("anno chiamato")
            self.dd1 = e.control.data
            squadre = self._model.getNodesAnno(int(self.dd1))
            self._view.aggiornaSquadre(squadre)
            self.loadNodes(self._view._ddSquadra)

            self._view.update_page()

    def loadNodes(self, dd: ft.Dropdown()):
        dd.options.clear()  # importantissimo

        if self.dd1 is None:
            return

        nodes = self._model.getNodesAnno(int(self.dd1))

        for squadra in nodes:
            dd.options.append(
                ft.dropdown.Option(
                    text=squadra.name,
                    data=squadra,
                    on_click=self.read_DD_Nodes
                )
            )

    def read_DD_Nodes(self, e):

        if e.control.data is None:
            self._node = None
        else:
            print("squadra chiamata ")
            self._node = e.control.data

    def getNodes(self):
        if self.dd1 is None:
            return []

        nodes = self._model.getNodesAnno(int(self.dd1))

        res = []
        for squadra in nodes:
            res.append(squadra)

        return res

    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()

        n = int(self.dd1)

        self._model.buildGraphPesato(n)

        self._view._txt_result.controls.append(
            ft.Text(f"il grafo creato ha {self._model.getNumNodi()} nodi")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"il grafo creato ha {self._model.getNumArchi()} archi")
        )

        self._view.update_page()

    def handleDettagli(self, e):

        if self._node is None:
            print("nessuna squadra selezionata")
            return

        print("Nodo scelto:", self._node.name)

        if self._node not in self._model._grafo:
            print("Nodo non presente nel grafo")
            return

        top5 = self._model.getTop5Edges(self._node)

        print(top5)

        self._view.mostraRisultati(top5)

    def handlePercorso(self, e):
        pass