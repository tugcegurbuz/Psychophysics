%%% This code calculates thresholds for each location at control and
%%% experimental trials and fits a logistic regression function. Then,
%%% plots the functions.

clc; clear;

% Initialize an array to store thresholds

thresholds = {{'Loc'}, {'controlT'}, {'scT'}};

% Go through each participant

k = 2;

for participant = 1:1
    figure();
    p = 1;
    %% Get the data from the combined data file

    file_path = ['....', num2str(participant), '...'];

    data_cell = readcell(file_path);

    %% Divide the data into control and staircase
    
    control_data = data_cell(:, 1:3);
    
    sc_data = data_cell(:, 4:6);

    %% Find thresholds in each location
    locations = {'....' };
    
    for l = 1:length(locations)
        
        % Get the location specific data
        
        location = locations{l}
        
        control_location_log = strcmp(control_data(:, 1), location);
        control_locations = control_data(:, 2:3);
        control_location_data = control_locations(strcmp(control_data(:, 1), location), 1:2);
        
        sc_location_log = strcmp(sc_data(:, 1), location);
        sc_locations = sc_data(:, 2:3);
        sc_location_data = sc_locations(sc_location_log, 1:2);
        
        
        % Stimulus instensities
    
        control_stimLevels = unique([control_location_data{2:end, 1}]);
        sc_stimLevels = unique([sc_location_data{2:end, 1}]);
        
        
        % Number of positive responses (e.g., 'right' at each of the 
        % entries of 'StimLevels'

        control_nCorrect = [];

        for i = 1:length(control_stimLevels)

            level = control_stimLevels(i);
            responses = {control_location_data{2:end, 2}};
            truth_array = level == [control_location_data{2:end, 1}];
            responsesLevel = {responses{truth_array}};
            nCorrect = nnz(strcmp(responsesLevel, 'right'));
            control_nCorrect = [control_nCorrect, nCorrect];

        end

        sc_nCorrect = [];

        for i = 1:length(sc_stimLevels)

            level = sc_stimLevels(i);
            responses = {sc_location_data{2:end, 2}};
            truth_array = level == [sc_location_data{2:end, 1}];
            responsesLevel = {responses{truth_array}};
            nCorrect = nnz(strcmp(responsesLevel, 'right'));
            sc_nCorrect = [sc_nCorrect, nCorrect];

        end
        
        
        % Number of trials at each entry of 'StimLevels'

        control_ntotal = [];

        for i = 1:length(control_stimLevels)

            level = control_stimLevels(i);
            ntotal = sum(level == [control_location_data{2:end, 1}]);
            control_ntotal = [control_ntotal, ntotal];
            
        end

        sc_ntotal = [];

        for i = 1:length(sc_stimLevels)

            level = sc_stimLevels(i);
            ntotal = sum(level == [sc_location_data{2:end, 1}]);
            sc_ntotal = [sc_ntotal, ntotal];
            
        end

        
        % Initialize Options
        
        options = struct;
        options.sigmoidName = 'logistic';
        options.exp.Type = 'equalAsymptote';
        options.fixedPars = [NaN, NaN, 0.01, NaN, NaN]; % (threshold, width, lapse, guess and eta)

        % Fit the results
        control_fit_data = [transpose(control_stimLevels), transpose(control_nCorrect), transpose(control_ntotal)];
        control_result = psignifit(control_fit_data, options);
        control_T = control_result.Fit(1);
        eta_c = control_result.Fit(5);
        var_c = eta_c * 0.5;
        fprintf('C: The expected value is in %s is 0.5, variance is %d', location, eta_c)
        sc_fit_data = [transpose(sc_stimLevels), transpose(sc_nCorrect), transpose(sc_ntotal)];
        sc_result = psignifit(sc_fit_data, options);
        sc_T = sc_result.Fit(1);
        eta_sc = sc_result.Fit(5);
        var_sc = eta_sc * 0.5;
        fprintf('SC: The expected value is in %s is 0.5, variance is %d', location, eta_sc)
        
        %psi.GoodnessOfFit(sc_result)
        % Store the thresholds
        thresholds(k, 1) = {location};
        thresholds(k, 2) = {control_T};
        thresholds(k, 3) = {sc_T};
        
        k = k + 1;
        
        %% Draw Psychometric Function
        subplot(3, 5, p)
        title(location)
        plotOptions.dataColor = [0, 0, 1];
        plotOptions.lineColor = [0, 0, 1];
        plotOptions.xLabel = 'Orientation (°)';
        plotOptions.yLabel = 'Proportion of Right';
        [hline1, hdata1] = plotPsych(control_result, plotOptions)
        hold on
        plotOptions.dataColor = [1, 0, 0];
        plotOptions.lineColor = [1, 0, 0];
        [hline2, hdata2] = plotPsych(sc_result, plotOptions)
        hold off
        
        if p == 15
            legend([hline1, hline2],'Control condition', 'Experimental condition')
        end
        p = p + 1;
    end
end
