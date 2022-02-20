/*

# ------------------------------ #
#                                #
#  version 0.0.1                 #
#                                #
#  Aleksiej Ostrowski, 2022      #
#                                #
#  https://aleksiej.com          #
#                                #
# ------------------------------ #  

*/

package main

import (
    "C"
    // "fmt"
    "image"
    "image/png"
    "os"
    // "io"
    "math/rand"
    "image/draw"
    "math"
)

var WIZARD = []float64 {0.2627, 0.678, 0.0593}

func main() {

}   

//export mix_two
func mix_two(one_image_C *C.char, two_image_C *C.char, save_image_C *C.char, s_C C.long) C.ulong {

    rand.Seed(int64(s_C))

    image.RegisterFormat("png", "png", png.Decode, png.DecodeConfig)

    one_image := C.GoString(one_image_C)
    two_image := C.GoString(two_image_C)
    save_image := C.GoString(save_image_C)

    file1, err := os.Open(one_image)

    if err != nil {
        return 0
    }

    defer file1.Close()

    img1, _, err := image.Decode(file1)

    if err != nil {
        return 0
    }

    file2, err := os.Open(two_image)

    if err != nil {
        return 0
    }

    defer file2.Close()

    img2, _, err := image.Decode(file2)

    if err != nil {
        return 0
    }

    bounds_one := img1.Bounds()
    // width_one, height_one := bounds_one.Max.X, bounds_one.Max.Y

    rgba_one := image.NewRGBA(bounds_one)
    draw.Draw(rgba_one, bounds_one, img1, bounds_one.Min, draw.Src)

    bounds_two := img2.Bounds()

    rgba_two := image.NewRGBA(bounds_two)
    draw.Draw(rgba_two, bounds_two, img2, bounds_two.Min, draw.Src)

    len_img1 := len(rgba_one.Pix)
    len_img2 := len(rgba_two.Pix)
    
    len_img1_d4 := len_img1 >> 2  

    mp := make(map[int]struct{}, len_img1_d4)

    var zero = struct{}{}
    n := 0
    var crc float64 = .0

    for {
        pset := rand.Intn(len_img1_d4)

        if _, ok := mp[pset]; ok {
            continue
        } else {
            mp[pset] = zero
            copy(rgba_one.Pix[pset << 2:], rgba_two.Pix[n:n+4]) 
            c := .0
            for i := n; i < n + 3; i++ {
                c += float64(rgba_two.Pix[i]) * WIZARD[i - n]
            }
            crc += c * float64(n + 1)
            n += 4
            if n >= len_img2 {
                break
            }
         }        
    }


    f, err := os.Create(save_image)
    if err != nil {
        return 0
    }

    defer f.Close()

    if err = png.Encode(f, rgba_one); err != nil {
        return 0
    }

    return C.ulong(math.Round(crc))
}


//export extract_two
func extract_two(one_image_C *C.char, width_two C.int, height_two C.int, save_image_C *C.char, s_C C.long) C.ulong {

    rand.Seed(int64(s_C))

    image.RegisterFormat("png", "png", png.Decode, png.DecodeConfig)

    one_image := C.GoString(one_image_C)
    save_image := C.GoString(save_image_C)

    file1, err := os.Open(one_image)

    if err != nil {
        return 0
    }

    defer file1.Close()

    img1, _, err := image.Decode(file1)

    if err != nil {
        return 0
    }

    bounds_one := img1.Bounds()

    rgba_one := image.NewRGBA(bounds_one)
    draw.Draw(rgba_one, bounds_one, img1, bounds_one.Min, draw.Src)

    len_img1 := len(rgba_one.Pix)
    len_img1_d4 := len_img1 >> 2  

    mp := make(map[int]struct{}, len_img1_d4)

    var zero = struct{}{}
    n := 0
    var crc float64 = .0

	rgba_two := image.NewRGBA(image.Rect(0, 0, int(width_two), int(height_two)))

    len_img2 := len(rgba_two.Pix)

    for {
        pset := rand.Intn(len_img1_d4)

        if _, ok := mp[pset]; ok {
            continue
        } else {
            mp[pset] = zero
            copy(rgba_two.Pix[n:n+4], rgba_one.Pix[pset << 2:])
            c := .0
            for i := n; i < n + 3; i++ {
                c += float64(rgba_two.Pix[i]) * WIZARD[i - n]
            }
            crc += c * float64(n + 1)
            n += 4
            if n >= len_img2 {
                break
            }
         }        
    }

    f, err := os.Create(save_image)
    if err != nil {
        return 0
    }

    defer f.Close()

    if err = png.Encode(f, rgba_two); err != nil {
        return 0
    }

    return C.ulong(math.Round(crc))
}
