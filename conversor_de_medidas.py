medida = float(input('Digite aqui a quantidade em METROS que deseja:\n>>>'));

cm = medida * 100;
mm = medida * 1000;
km = medida / 1000;

print(f'{medida}m, corresponte à \n{mm} mm \n{cm} cm \n{km} km');
