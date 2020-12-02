import click

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        pkg_dimensions = f.read().splitlines()

    material_needed = 0
    ribbon_needed = 0

    for pkg_dimension in pkg_dimensions:
        values = pkg_dimension.split('x')
        # print(values)
        l = int(values[0])
        w = int(values[1])
        h = int(values[2])
        area_pairs = [l*w, w*h, h*l]
        perimeters = [2*l+2*w, 2*w+2*h, 2*h+2*l]
        volume = l*w*h
        surface_area = 0
        min = 100000000
        for pair in area_pairs:
            work_surface = 2 * pair
            if pair < min:
                min = pair
            surface_area += work_surface
        # print(f"Surface Area: {surface_area}")
        material_needed += surface_area + min

        min = 100000000
        for perimeter in perimeters:
            if perimeter < min:
                min = perimeter

        ribbon_needed += min + volume

    print(f"Material needed: {material_needed}")
    print(f"Ribbon needed: {ribbon_needed}")

if __name__ == "__main__":
    main()