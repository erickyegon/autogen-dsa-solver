# Professional R Template for DSA Solutions
# Enhanced with comprehensive error handling and statistical computing capabilities

# Load required libraries
suppressMessages({
  if (!require(tidyverse, quietly = TRUE)) install.packages("tidyverse")
  if (!require(data.table, quietly = TRUE)) install.packages("data.table")
  library(tidyverse)
  library(data.table)
})

#' Professional DSA Solution Template in R
#' 
#' This template provides robust error handling and statistical computing
#' capabilities for Data Structures and Algorithms problems
#' 
#' @param input_data Problem input data
#' @return Solution result or NULL if error occurs
#' 
#' Time Complexity: O(?)
#' Space Complexity: O(?)
solve_dsa_problem <- function(input_data) {
  
  # Input validation with comprehensive error handling
  tryCatch({
    
    # Validate input is not NULL
    if (is.null(input_data)) {
      stop("Input cannot be NULL")
    }
    
    # Type checking based on expected input
    if (!is.vector(input_data) && !is.matrix(input_data) && !is.data.frame(input_data)) {
      stop(paste("Expected vector, matrix, or data.frame, got", class(input_data)[1]))
    }
    
    # Handle edge cases
    edge_result <- handle_edge_cases(input_data)
    if (!is.null(edge_result)) {
      return(edge_result)
    }
    
    # Main algorithm implementation
    result <- main_algorithm(input_data)
    
    cat("✅ Algorithm executed successfully!\n")
    return(result)
    
  }, error = function(e) {
    cat("❌ Error:", e$message, "\n")
    cat("💡 Suggestion: Check input data format and constraints\n")
    return(NULL)
  }, warning = function(w) {
    cat("⚠️ Warning:", w$message, "\n")
    # Continue execution for warnings
  })
}

#' Handle common edge cases for R data structures
#' 
#' @param data Input data to check
#' @return Result for edge case or NULL if not an edge case
handle_edge_cases <- function(data) {
  
  # Empty data
  if (length(data) == 0) {
    cat("🔍 Edge case: Empty input detected\n")
    return(vector())  # Return empty vector
  }
  
  # Single element
  if (length(data) == 1) {
    cat("🔍 Edge case: Single element detected\n")
    return(data)
  }
  
  # All NA values
  if (all(is.na(data))) {
    cat("🔍 Edge case: All NA values detected\n")
    return(NA)
  }
  
  return(NULL)  # Not an edge case
}

#' Main algorithm implementation
#' 
#' @param data Validated input data
#' @return Algorithm result
main_algorithm <- function(data) {
  
  # Example: Statistical algorithm implementation
  # Replace this with your specific algorithm
  
  # Step 1: Data preprocessing
  processed_data <- preprocess_data(data)
  
  # Step 2: Core algorithm logic
  result <- core_algorithm(processed_data)
  
  # Step 3: Post-processing and validation
  final_result <- postprocess_result(result)
  
  return(final_result)
}

#' Preprocess input data for algorithm
#' 
#' @param data Raw input data
#' @return Preprocessed data
preprocess_data <- function(data) {
  
  # Remove NA values if present
  if (any(is.na(data))) {
    cat("🔧 Removing NA values from input\n")
    data <- data[!is.na(data)]
  }
  
  # Convert to appropriate data type if needed
  if (is.character(data)) {
    # Try to convert to numeric if possible
    numeric_data <- suppressWarnings(as.numeric(data))
    if (!any(is.na(numeric_data))) {
      data <- numeric_data
      cat("🔧 Converted character data to numeric\n")
    }
  }
  
  return(data)
}

#' Core algorithm implementation
#' 
#' @param data Preprocessed data
#' @return Algorithm result
core_algorithm <- function(data) {
  
  # Example: Sorting algorithm with statistical analysis
  # Replace with your specific algorithm
  
  # Sort the data
  sorted_data <- sort(data)
  
  # Calculate statistical measures
  stats <- list(
    sorted = sorted_data,
    mean = mean(sorted_data),
    median = median(sorted_data),
    sd = sd(sorted_data),
    min = min(sorted_data),
    max = max(sorted_data)
  )
  
  return(stats)
}

#' Post-process algorithm result
#' 
#' @param result Raw algorithm result
#' @return Final processed result
postprocess_result <- function(result) {
  
  # Validate result structure
  if (is.null(result)) {
    stop("Algorithm returned NULL result")
  }
  
  # Add metadata
  result$timestamp <- Sys.time()
  result$r_version <- R.version.string
  
  return(result)
}

#' Run comprehensive test suite
#' 
#' @return TRUE if all tests pass, FALSE otherwise
run_comprehensive_tests <- function() {
  
  cat("🧪 RUNNING COMPREHENSIVE TEST SUITE\n")
  cat(paste(rep("=", 50), collapse = ""), "\n")
  
  # Define test cases
  test_cases <- list(
    list(
      input = numeric(0),
      expected_type = "logical",  # Empty vector
      description = "Empty input"
    ),
    list(
      input = c(5),
      expected_type = "numeric",
      description = "Single element"
    ),
    list(
      input = c(3, 1, 4, 1, 5, 9, 2, 6),
      expected_type = "list",
      description = "Normal numeric vector"
    ),
    list(
      input = c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
      expected_type = "list",
      description = "Reverse sorted data"
    ),
    list(
      input = c(1, 1, 1, 1, 1),
      expected_type = "list",
      description = "All identical elements"
    )
  )
  
  passed <- 0
  total <- length(test_cases)
  
  for (i in seq_along(test_cases)) {
    test_case <- test_cases[[i]]
    
    cat("\n📋 Test Case", i, ":", test_case$description, "\n")
    cat("📥 Input:", toString(test_case$input), "\n")
    
    # Run the algorithm
    result <- solve_dsa_problem(test_case$input)
    
    # Check if result type matches expected
    if (!is.null(result) && class(result)[1] == test_case$expected_type) {
      cat("✅ PASSED\n")
      passed <- passed + 1
    } else if (is.null(result) && test_case$expected_type == "null") {
      cat("✅ PASSED (Expected NULL)\n")
      passed <- passed + 1
    } else {
      cat("❌ FAILED\n")
      cat("💡 Expected type:", test_case$expected_type, "Got:", class(result)[1], "\n")
    }
  }
  
  cat("\n📊 TEST RESULTS:", passed, "/", total, "tests passed\n")
  
  if (passed == total) {
    cat("🎉 ALL TESTS PASSED!\n")
    return(TRUE)
  } else {
    cat("⚠️", total - passed, "tests failed\n")
    return(FALSE)
  }
}

#' Display algorithm complexity analysis
display_complexity_analysis <- function() {
  cat("\n⚡ COMPLEXITY ANALYSIS:\n")
  cat("Time Complexity: O(n log n) - due to sorting operation\n")
  cat("Space Complexity: O(n) - for storing sorted data and statistics\n")
  
  cat("\n💡 OPTIMIZATION OPPORTUNITIES:\n")
  cat("- Use data.table for large datasets (faster operations)\n")
  cat("- Implement parallel processing with parallel package\n")
  cat("- Use specialized statistical packages for domain-specific algorithms\n")
  
  cat("\n🔍 R-SPECIFIC ADVANTAGES:\n")
  cat("- Built-in statistical functions and distributions\n")
  cat("- Excellent data manipulation with tidyverse\n")
  cat("- Advanced visualization capabilities with ggplot2\n")
  cat("- Specialized packages for mathematical optimization\n")
}

#' Main execution function
main <- function() {
  cat("🚀 PROFESSIONAL R DSA SOLUTION\n")
  cat(paste(rep("=", 40), collapse = ""), "\n")
  
  # Run comprehensive tests
  success <- run_comprehensive_tests()
  
  if (success) {
    # Display complexity analysis
    display_complexity_analysis()
    
    cat("\n🎯 R LANGUAGE STRENGTHS FOR DSA:\n")
    cat("- Statistical computing and data analysis\n")
    cat("- Mathematical optimization problems\n")
    cat("- Large dataset processing\n")
    cat("- Probability and combinatorics problems\n")
    cat("- Machine learning algorithm implementation\n")
    
    cat("\n📚 RECOMMENDED R PACKAGES FOR DSA:\n")
    cat("- data.table: Fast data manipulation\n")
    cat("- Rcpp: C++ integration for performance\n")
    cat("- igraph: Graph algorithms and analysis\n")
    cat("- lpSolve: Linear programming optimization\n")
    cat("- combinat: Combinatorial mathematics\n")
  }
  
  cat("\nSTOP\n")  # Termination signal for AutoGen
}

# Execute main function
if (!interactive()) {
  main()
}
