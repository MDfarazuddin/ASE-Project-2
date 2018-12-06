n = -20:20;
xn = Signal_Tan(n);
stem(n,xn);


f_tan  = fft(xn(abs(n)<5));
if_tan = ifft(f_tan);


%%%%%%%%%%%%%%%%%%%%%%%%%%

ko = pi;
N = 10;
n1 = 0:N;
figure;
xn1 = zeros(size(n1));
xn1(1:end) = exp(1j*2*pi*ko*1/N);
stem(abs(xn1));

plot(abs(fftshift(fft(xn1))));
figure;
plot(angle(fftshift(fft(xn1))));

%%%%%%%%%%%%%%%%%%%%%%%%%%

x2n = [0 1 0 0 0];
x1n = [0 1 2 3 4];
sn = [1 0 0 0 0];
figure;
stem(x1n)



f_x1n = fft(x1n,5);
f_x2n = fft(x2n,5);
f_sn = fft(sn,5);

yn = f_x1n .* f_x2n;
yn = ifft(yn);
% cc = cconv(x1n,x2n,5);

fx3n = (f_x1n.')';

 for i = 1:length(fx3n)
    fx3n(i) = fx3n(i)/abs(fx3n(i))^2;
 end

figure;
stem(x2n)
figure;
stem(yn);
figure;
stem(fx3n)