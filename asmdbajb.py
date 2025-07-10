                                  command=lambda fila=i, col=j: self.marcar(fila, col))
                boton.grid(row=i, column=j)
                self.botones[i][j] = boton

    def marcar(self, fila, col):
        boton = self.botones[fila][col]
        if boton["text"] == "":
            boton["text"] = self.turno
            if self.verificar_ganador():
                messagebox.showinfo("¡Fin del juego!", f"¡{self.turno} ha ganado!")
                self.reiniciar_tablero()
            elif self.verificar_empate():
                messagebox.showinfo("Empate", "¡Nadie ganó!")
                self.reiniciar_tablero()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        b = self.botones
        # Revisar filas, columnas y diagonales
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != "":
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            return True
        return False

    def verificar_empate(self):
        for fila in self.botones:
            for boton in fila:
                if boton["text"] == "":
                    return False
        return True

    def reiniciar_tablero(self):
        for fila in self.botones:
            for boton in fila:
                boton.config(text="")
        self.turno = "X"

# Ejecutar el juego
if __name__ == "__main__":
    ventana = tk.Tk()
    juego = Gato(ventana)
    ventana.mainloop()
