/*
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
*/
#include <iostream>
using namespace std;
float percentage(float numero,float soma){
    float resultado;
    resultado = (numero/soma)*100.00;
    return resultado;
}
int main(){
    float sp = 67836.43;
    float rj = 36678.66;
    float mg = 29229.88;
    float es = 27165.48;
    float outros = 19849.53;
    float soma = sp+rj+mg+es+outros;
    cout << "Percentual de SP: "<< percentage(sp,soma) <<" %"<< endl;
    cout << "Percentual de RJ: "<< percentage(rj,soma) <<" %"<< endl;
    cout << "Percentual de MG: "<< percentage(mg,soma) <<" %"<< endl;
    cout << "Percentual de ES: "<< percentage(es,soma) <<" %"<< endl;
    cout << "Percentual de Outros estados: "<< percentage(outros,soma) <<" %"<< endl;
    return 0;
}
// Favor executar quartoDesafio.exe