%% This function creates a heatmap of the TAE magnitudes

clc; clear;
%% Get the data
tae_data_path = '...';
tae_data_cell = readcell(tae_data_path);
%% Create x (x-axis), y (y-axis), z (TAE) variables
%Initialize variables
x = []; y = []; z = [];
%Go through all locations column by column
for loc = 1:15
    %Get TAEs
    TAE = [tae_data_cell{2:20, loc}];
    %Get the temp location
    temp_loc = tae_data_cell{1, loc};
    %Get test location and meridian
    test_loc = temp_loc(2:end);
    mer = temp_loc(1);
    %Test location loop
    if strcmp(test_loc, 'Near1')
        X = 2.5;
    elseif strcmp(test_loc,'Near2')
        X = 6.5;
    elseif strcmp(test_loc, 'Center')
        X = 10.5;
    elseif strcmp(test_loc, 'Further1')
        X = 14.5;
    elseif strcmp(test_loc, 'Further2')
        X = 18.5;
    end
    %Meridian loop
    if mer == 'u'
        Y = 4;
    elseif mer == 'c'
        Y = 0;
    elseif mer == 'd'
        Y = -4;
    end
    %TAE loop
    for i = 1:19
        temp_TAE = TAE(i);
        z = [z; temp_TAE];
        x = [x; X];
        y = [y; Y];
    end
end
%% Create the heatmap
load('.../mycolormap2.mat')
[x_mesh, y_mesh] = meshgrid(x, y);
[x2_mesh, y2_mesh] = meshgrid(0:0.1:20, -10:0.1:10);
int_data = griddata(x, y, z, x2_mesh, y2_mesh, 'natural');

surf(x2_mesh, y2_mesh, int_data)

shading interp

colormap(mymap)
cbar = colorbar;
cbar.Location = 'northoutside';
cbar.Label.String = 'TAE Magnitude';
caxis([0 10])
brighten(.3)

xlim([0 20])
names_x = {'Near1', 'Near2', 'Center', 'Further1', 'Further2'};
set(gca,'xtick',[2.5:4:20.5],'xticklabel',names_x)
ylim([-8, 8])
names_y = {'-8', 'Down', 'Center', 'Up', '8'};
set(gca,'ytick',[-8:4:8],'yticklabel',names_y, 'FontSize', 20)

grid on
ax.GridAlpha = 1;
hold on
%Put test locations and significance
sig = {'n.s.', '***', '**', '*', '***', '**', '***', '***', '***', '**', '***', '**', '*', '***', '*'};
t_ind = 1;
for i = [2.5:4:18.5]
    for j = [-4:4:4]
        if i == 10.5 && j == 0
            plot3(i, j, 10, 'ko', 'MarkerSize', 70,'LineWidth', 5)
        else
            plot3(i, j, 10, 'ko', 'MarkerSize', 70)
        end
        t = text(i, j, 10, sig{t_ind})
        t.FontSize = 18;
        t.HorizontalAlignment = 'center';
        t.FontWeight = 'bold';
        t.FontName = 'times';
        t_ind = t_ind + 1;
    end
end

%Put fixation
plot3(0.02, 0, 10, 'k+', 'MarkerSize', 13, 'LineWidth', 5)
