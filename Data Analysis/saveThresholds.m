%%%% This code saves the thresholds into an excel file for the independent
%%%% t-test that will be done to compare the the adaptation index between
%%%% visual fields 
%%%% adaptationInd = threshold_adaptation - threshold_control


clc; clear;

%%% Initialize the location list in the experiment
locations = {'...' };


%%% Initialize an array to store adaptation index

aInds = {};
vfs = {'aIndLeft', 'aIndRight'};

for v = 1:2
    
    vf = char(vfs(v));
    
    for n = 1:length(locations)
        
        loc = char(locations(n));
        aInd_col_name = [vf, '_', loc];
        aInds{1, end + 1} = aInd_col_name;
        
    end
end

%%% Go through each participant
participant_list = [...]; 

for p_ind = 1:length(participant_list)
    
    participant = participant_list(p_ind);

    %% Get the data from the combined data file

    file_path = ['./', num2str(participant), '_Combined.xlsx'];

    data_cell = readcell(file_path);

    %% Divide the data into control and staircase
    
    control_data = data_cell(:, 1:3);
    
    sc_data = data_cell(:, 4:6);

    %% Find thresholds in each location
    
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
        options.fixedPars = [NaN, NaN, .01, 0, 0]; % (threshold, width, lapse, guess and eta)

        % Fit the results
        control_fit_data = [transpose(control_stimLevels), transpose(control_nCorrect), transpose(control_ntotal)];
        control_result = psignifit(control_fit_data, options);
        control_T = control_result.Fit(1);
        
        sc_fit_data = [transpose(sc_stimLevels), transpose(sc_nCorrect), transpose(sc_ntotal)];
        sc_result = psignifit(sc_fit_data, options);
        sc_T = sc_result.Fit(1);
        
            
        % Find adaptation index
        aInd = {sc_T - control_T};
        
        % Store adaptation index
        % Note: even ps numbers: Left VF, odd ps numbers: Right VF
        if mod(participant, 2) == 0
            store_col = ['aIndLeft', '_', location];
        else
            store_col = ['aIndRight', '_', location];
        end
        
    col_ind = find(contains(aInds(1, :), store_col));
    
    if p_ind == 1
        row_ind = 2;
    else
        row_ind = find(cellfun('isempty', aInds(:, col_ind)), 1)
    end
    
    if isempty(row_ind)
        [n_row, n_col] = size(aInds);
        row_ind = n_row + 1;
    end
    
    aInds(row_ind, col_ind) = aInd;


    end
end

%%% Save to excel file
filename = ['aIndsVF.xlsx'];
T = cell2table(aInds(2:end,:),'VariableNames', aInds(1,:))
 
% Write the table to a CSV file
writetable(T,filename)

