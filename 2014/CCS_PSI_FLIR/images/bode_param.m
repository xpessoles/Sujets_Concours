clear all
close all


Ti=0.1;
Ti2=0.01;
T1=0.75;
T2=1.6*1e-3;

scrsz = get(0,'ScreenSize');

wf=8/10;
hf=4/5;
figsize=[0 0  0.4*scrsz(3) 0.9*scrsz(4)];

%Diagramme de Bode;

varlogw=-2:0.001:3;
varw=10.^(varlogw);
Kt=1;
lwc=[1/T1,1/Ti,1/T2];
ordre=([1,-1,1]);
wc_ordre=sortrows([lwc;ordre]');
lwc=wc_ordre(:,1);
ordre=wc_ordre(:,2);

%HBO1
HBO1=Kt./(Ti*i*varw);
asymp1=Kt./(i*Ti*varw);
k=1;
for wc=lwc'
    wc
    asymp1(find(varw>wc))=asymp1(find(varw>wc))./(i*varw(find(varw>wc))/wc).^(ordre(k));
    if abs(ordre(k))<=1
    HBO1=HBO1.*(1+i*varw/wc).^(-ordre(k));
    end  
    k=k+1;
end
asymp1=20*log(Kt.*asymp1)./log(10);
vphi1=angle(HBO1)*180/pi;
vphi1(find(vphi1>=0))=vphi1(find(vphi1>=0))-360;
phi_asymp1=-90*ones(1,length(varw));
k=1;
for wc=lwc'
    phi_asymp1(find(varw>wc))=phi_asymp1(find(varw>wc))-ordre(k)*90*ones(1,length(varw(find(varw>wc))));
    k=k+1;
end

lwc2=[1/T1,1/Ti2,1/T2];
ordre2=([1,-1,1]);
wc_ordre2=sortrows([lwc2;ordre2]');
lwc2=wc_ordre2(:,1);
ordre2=wc_ordre2(:,2);

%HBO1
HBO2=Kt./(Ti2*i*varw);
asymp2=Kt./(i*Ti2*varw);
k=1;
for wc=lwc2'
    wc
    asymp2(find(varw>wc))=asymp2(find(varw>wc))./(i*varw(find(varw>wc))/wc).^(ordre2(k));
    if abs(ordre2(k))<=1
    HBO2=HBO2.*(1+i*varw/wc).^(-ordre2(k));
    end  
    k=k+1;
end
asymp2=20*log(Kt.*asymp2)./log(10);
vphi2=angle(HBO2)*180/pi;
vphi2(find(vphi2>=0))=vphi2(find(vphi2>=0))-360;
phi_asymp2=-90*ones(1,length(varw));
k=1;
for wc=lwc2'
    wc
    phi_asymp2(find(varw>wc))=phi_asymp2(find(varw>wc))-ordre2(k)*90*ones(1,length(varw(find(varw>wc))));
    k=k+1;
end
% HBO2=HBO1*Kp2;
% asymp2=asymp1+20*log(Kp2)./log(10);



figure1=figure('position',figsize)
for k=[1,2,3]
axes1=subplot(2,1,1,'parent',figure1,'YGrid','on',...
    'XScale','log',...
    'XMinorTick','on',...
    'XMinorGrid','on',...
    'XGrid','on',...
'fontsize',20);
%box(axes1,'on');
%hold(axes1,'all');

if k==2
semilogx(varw,20*log(abs(HBO1))/log(10),'b-','linewidth',2)
hold on
semilogx(varw,20*log(abs(HBO2))/log(10),'r--','linewidth',2)
elseif k==3
hold on
semilogx(varw,asymp1,'b--','linewidth',2)
semilogx(varw,asymp2,'r--','linewidth',2)  
for wc=lwc'
line([wc,wc],[-300,300],'color','k','linestyle','--','LineWidth',1);
end
% semilogx(varw,20*log(abs(HBO2))/log(10),'r-','linewidth',5)
% hold on
% semilogx(varw,asymp2,'r--','linewidth',3)   
end
xlim([10^(varlogw(1)) 10^(varlogw(end))])
ylim([-150 100])
set(axes1,'ytick',[-150:50:100])
grid on
set(axes1,'FontSize',15)
xlabel('$\omega (rad\cdot s^{-1})$','fontsize',15,'interpreter','latex');
ylabel('$G (dB)$','fontsize',15,'interpreter','latex');
if k==2
legend('T_{ife}=0,1 s','T_{ife}=0,01 s')
end

axes2=subplot(2,1,2,'parent',figure1,'ygrid','on',...
    'xscale','log',...
    'xminortick','on',...
    'xminorgrid','on',...
    'xgrid','on',...
'fontsize',20)
%box(axes1,'on');
%hold(axes1,'all');
if k==2
semilogx(varw,vphi1,'b-','linewidth',2)
hold on
semilogx(varw,vphi2,'r--','linewidth',2)
elseif k==3
semilogx(varw,phi_asymp1,'k--','linewidth',2)
semilogx(varw,phi_asymp2,'r--','linewidth',2)
for wc=lwc'
line([wc,wc],[-300,300],'color','k','linestyle','--','LineWidth',1);
end
end
set(axes2,'ytick',-180:20:-80,'fontsize',15)
axis([10^(varlogw(1)) 10^(varlogw(end)) -180 -80])
grid on
xlabel('$\omega (rad\cdot s^{-1})$','fontsize',15,'interpreter','latex');
ylabel('$\varphi (^{\circ})$','fontsize',15,'interpreter','latex');

set(figure1,'paperpositionmode','auto');
if k==1
print('-depsc','bode_total0');
elseif k==2
%legend('H_{BO1}','H_{BO2}')
print('-depsc','bode_total');
elseif k==3
%legend('H_{BO1}','H_{BO2}')
print('-depsc','bode_total3');  
end
end

