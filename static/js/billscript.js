//for serial number
let count = 1;

function addMedicine() {
    let medicine = document.getElementById("medicine").value;
    let qty = Number(document.getElementById("qty").value);

    let medindex = medicine_name_list.indexOf(medicine);
    
    let unitprize = medicine_price_list[medindex];    

    let amt = qty * unitprize;
    let exp = medicine_expiry_list[medindex];

    let items = document.getElementById("itemlist").value;
    let quantity = document.getElementById("quantitylist").value;
    let total = document.getElementById("totalammount").value;


    //to prevent comma before text
    //if we excute code in else part for first element the element value will be ""+", "+"meddicine name" which will add comma
    // we dont want thant so writing this login


    if (count == 1) {
        document.getElementById("itemlist").value = medicine;
        document.getElementById("quantitylist").value = qty;
        document.getElementById("totalammount").value = Math.ceil(amt);
    }
    else {
        document.getElementById("itemlist").value = items + ", " + medicine;
        document.getElementById("quantitylist").value = quantity + ", " + qty;
        document.getElementById("totalammount").value =Math.ceil(parseFloat(total) + parseFloat(amt));
    }


    html = ` <tr>
    <td style="width:100px; padding:10px 20px">`+ count + `</td>
    <td style="width:100px; padding:10px 20px">`+ medicine + `</td>
    <td style="width:100px; padding:10px 20px">`+ qty + `</td>
    <td style="width:100px; padding:10px 20px">`+ exp +`</td>
    <td style="width:100px; padding:10px 20px">`+ unitprize + `</td>
    <td style="width:100px; padding:10px 20px">`+ amt + `</td>
    </tr>
    `;

    innerhtml = document.getElementById("description").innerHTML;
    document.getElementById("description").innerHTML = innerhtml + html;

    document.getElementById("submitButton").disabled = false;

    count++;

 
}


function clearAll() {
    document.getElementById("submitButton").disabled = true;
    count = 1;
    document.getElementById("itemlist").value = "";
    document.getElementById("quantitylist").value = "";
    document.getElementById("totalammount").value = "";
    document.getElementById("description").innerHTML = `<tr style="border: 2px solid black;">
    <th style="width:100px; padding:5px 20px">Sr. No.</th>
    <th style="width:400px; padding:5px 20px">Description</th>
    <th style="width:50px;  padding:5px 20px">Qty</td>
    <th style="width:200px; padding:5px 20px">Expiry</th>
    <th style="width:200px; padding:5px 20px">Unit Prize</th>
    <th style="width:200px; padding:5px 20px">Amount</th>
    </tr>
    <tr>
        <td style="width:100px; padding:10px 20px"></td>
        <td style="width:100px; padding:10px 20px"><input type="text"
        class="form-control w-100 border-2 border-dark" id="medicine" placeholder="Enter Medicine Name"></td>
        <td style="width:100px; padding:10px 20px"><input type="number" class="form-control w-100 border-2 border-dark" id="qty" value="1"></td>
        <td style="width:200px; padding:10px 20px"><button type="button" class="btn btn-primary w-100" onclick="addMedicine();">Add to list</button></td>
        <td style="width:100px; padding:10px 20px"><button type="reset" class="btn btn-danger" onclick="clearAll();">Clear All</button></td>
    </tr>`;


  
}


function submitButton(){
    document.getElementById("billform").submit();
}


function resetButton(){
    document.getElementById("pname").value = "";
    document.getElementById("page").value = "";
    document.getElementById("pmob").value = "";
    document.getElementById("drname").value = "";
    document.getElementById("hospitalname").value = "";
}



