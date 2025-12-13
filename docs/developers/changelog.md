# Changelog

## V2.0.0 - New Release

!!! warning "Breaking Changes"
    Sparck has now the ossial library included, but the abstractions have been renamed to avoid conflicts with the original ones. This has the following impact: All Max patches that have used Sparck nodes have to be modified before loading with max inside a text editor:
    
        - Open the Max patch file (.maxpat) with a text editor
        - Search for "ossia.device sparck" and replace it with "sparck.device sparck"
        - Save the file
        - Load the modified Max patch in Max

